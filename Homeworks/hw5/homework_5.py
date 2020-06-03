import psycopg2
import psycopg2.extras
from psycopg2 import sql
from data_structures import RecipeInstructions


class RestaurantData:

    def __init__(self, connection_string):
        self.conn = psycopg2.connect(connection_string)

    def check_connectivity(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM recipe LIMIT 1")
        records = cursor.fetchall()
        return len(records) == 1

    def find_recipe(self, recipe_name):
        recipe_name.lower()
        #query = sql.SQL("SELECT * FROM recipe WHERE lower(name) LIKE {rName}").format(rName = sql.Identifier(recipe_name))
        query = "SELECT * FROM recipe WHERE lower(name) LIKE '%%' || %s || '%%';"
        allRecipes = []
        with self.conn.cursor() as cursor:
            cursor.execute(query, (recipe_name, ))
            self.conn.commit()
            recipes = cursor.fetchall()
            for results in recipes:
                newdict = {"name": results[0],
                           "instructions": results[1],
                           "servings": results[2],
                           "course": results[3],
                           "season": results[4]}
                allRecipes.append(newdict)
            return allRecipes

    def get_recipe_instructions(self, recipe_name):
        query1 = "SELECT instructions FROM recipe WHERE name = '" + recipe_name + "'"
        query2 = "SELECT ingredient, amount FROM recipe_ingredient WHERE recipe = '" + recipe_name + "'"
        query3 = "SELECT name FROM ingredient WHERE code = %s"
        ingredients = []
        with self.conn.cursor() as cursor:
            cursor.execute(query1)
            self.conn.commit()
            instructions = cursor.fetchone()[0]
            cursor.execute(query2)
            self.conn.commit()
            ingreds = cursor.fetchall()
            for results in ingreds:
                cursor.execute(query3, (results[0], ))
                self.conn.commit()
                name = cursor.fetchone()[0]
                food = (name, results[1])
                ingredients.append(food)
        fullInstructions = RecipeInstructions(recipe_name, instructions, ingredients)
        return(fullInstructions)

    def get_seasonal_menu(self, season):
        query1 = "SELECT name, isKosher FROM \
            (SELECT recipe, count(distinct(is_kosher)) as isKosher FROM \
                recipe_ingredient INNER JOIN ingredient \
                ON recipe_ingredient.ingredient = ingredient.code \
                group by recipe \
            ) koshFoods \
            INNER JOIN recipe on recipe.name = koshFoods.recipe \
            WHERE season = 'All' \
            or season ='" + season + \
                "';"
        returnList = []
        with self.conn.cursor() as cursor:
            cursor.execute(query1)
            self.conn.commit()
            kosherFoods = cursor.fetchall()
            for foods in kosherFoods:
                #print(foods)
                if foods[1] == 1 : newTup = (foods[0], True)
                else: newTup = (foods[0], False)
                #print(newTup)
                returnList.append(newTup)
        return(returnList)


    def update_ingredient_price(self, ingredient_code, price):
        query = "WITH rows AS ( \
                UPDATE ingredient \
                SET cost_per_unit = " + str(price) +\
                "WHERE code = '%s' RETURNING 1 \
                ) select count(*) FROM rows;" % ingredient_code
        with self.conn.cursor() as cursor:
            cursor.execute(query)
            self.conn.commit()
            count = cursor.fetchone()[0]
        return(count)

    def add_new_recipe(self, recipe_instructions, servings, course, season):
        allIngreds = []
        for food in recipe_instructions.ingredients:
            query1 = "SELECT code FROM ingredient WHERE name = '" + food[0] + "';"
            with self.conn.cursor() as cursor:
                cursor.execute(query1)
                self.conn.commit()
                if cursor.rowcount == 0: return(False)
                else:
                    code = cursor.fetchone()[0]
                    allIngreds.append(code)
        query3 = "INSERT INTO recipe(name, instructions, servings, course, season)\
                    VALUES(" \
                        + "'" + recipe_instructions.name + "', " \
                        + "'" + recipe_instructions.instructions + "', " \
                        + "%i, " % servings \
                        + "'" + course + "', " \
                        + "'" + season + "');"
        with self.conn.cursor() as cursor:
            cursor.execute(query3)
            self.conn.commit()
            for i in range(len(allIngreds)):
                query2 = "INSERT INTO recipe_ingredient(ingredient, recipe, amount)\
                    VALUES (" \
                    + allIngreds[i] + ", " \
                    + "'" + recipe_instructions.name \
                    + "', %f);" % recipe_instructions.ingredients[i][1]
                cursor.execute(query2)
                self.conn.commit()
        return(True)





