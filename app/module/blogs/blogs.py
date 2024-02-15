from app.model.connect_to_db import ConnectDB


# This class is used to perform all the blogs operations
class Blogs(object):

    def __init__(self):
        self.desc = "All Blogs Operations"
        self.collection_name = "blogs"

    # This function is used to create a blog
    def create_blog(self, data):
        """
        This function is used to create a blog
        :param blog_data:
        :return:
        """
        try:
            # create a dictionary of the blog data
            blog_dict = {
                "title": data.get('title', ""),
                "description": data.get('description', "")
            }

            # connect to the database and insert the blog_dict
            ConnectDB().connect_db()[self.collection_name].insert_one(blog_dict)

            # return a success message
            return {"status": "success", "message": "Blog created successfully"}
        except Exception as e:
            # return a failure message
            return {"status": "failure", "message": str(e)}

    # to update the blog

    def update_blog(self, data):
        print(data)
        """
        This function is used to update a blog
        :param blog_id: Identifier of the blog to update
        :param data: Updated data for the blog
        :return: Status message
        """
        try:
            # create a dictionary of the updated blog data
            updated_data = {
                "$set": {
                    "title": data.get('title', ""),
                    "description": data.get('description', "")
                }
            }

            # connect to the database and update the blog entry
            ConnectDB().connect_db()[self.collection_name].update_one({"title": data.get('title', "")}, updated_data)

            # return a success message
            return {"status": "success", "message": "Blog updated successfully"}
        except Exception as e:
            # return a failure message
            return {"status": "failure", "message": str(e)}

    def delete_blog(self, data):
        try:
            delete_data = {
                "$set": {
                    "title": data.get('title', ""),
                    "description": data.get('description', "")
                }

            }
            ConnectDB().connect_db()[self.collection_name].delete_one(data)
            return {"status": "success", "message": "Blog deleted successfully"}
        except Exception as e:
            return {"status": "failure", "message": str(e)}

    def create_multiple_blog(self, data):
        try:
            new_blog = data if isinstance(data, list) else [data]
            ConnectDB().connect_db()[self.collection_name].insert_many(new_blog)
            return {"status": "success", "message": "Blog created successfully"}
        except Exception as e:
            return {"status": "failure", "message": str(e)}

    # def get_all_blogs(self, data):
    #     try:
    #         all_blogs = ConnectDB().connect_db()
    #         all_blogs[self.collection_name].find()
    #         # all_blogs_cursor = list(all_blogs)
    #         return {"status": "success", "Blogs retrieved": "Blogs retrieved"}
    #     except Exception as e:
    #         return {"status": "failure", "message": str(e)}

    # def get_all_blogs(self):
    #     try:
    #         # Connect to the database and retrieve all blogs
    #         all_blogs_cursor = ConnectDB().connect_db()[self.collection_name].find()
    #
    #         # Convert the cursor to a list of dictionaries
    #         all_blogs = list(all_blogs_cursor)
    #         print(all_blogs)
    #         return {"status": "success", "blogs": all_blogs}
    #     except Exception as e:
    #         return {"status": "failure", "message": str(e)}
