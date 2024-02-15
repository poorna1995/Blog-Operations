from app import app
from app.module.blogs.blogs import Blogs
from flask import jsonify, request


# This is the route used to create a blog
@app.route('/create_blog', methods=['POST'])
def create_blog():
    """
    This function is used to create a blog
    :return:
    """
    try:
        # get the data from the request
        data = request.get_json()

        # call the create_blog function from the Blogs class
        response = Blogs().create_blog(data)

        # return the response
        return jsonify(response)
    except Exception as e:
        return jsonify({"status": "failure", "message": str(e)})


@app.route('/update_blog', methods=['PUT'])
def update_blog():
    try:
        data = request.get_json()
        response = Blogs().update_blog(data)
        return jsonify(response)
    except Exception as e:
        return jsonify({"status": "failure", "message": str(e)})


@app.route('/delete_blog', methods=['DELETE'])
def delete_blogs():
    try:
        data = request.get_json()
        response = Blogs().delete_blog(data)
        return jsonify(response)
    except Exception as e:
        return jsonify({"status": "failure", "message": str(e)})


@app.route('/create_multiple_blog', methods=['POST'])
def create_multiple_blog():
    try:
        data = request.get_json()
        response = Blogs().create_multiple_blog(data)
        return jsonify(response)
    except Exception as e:
        return jsonify({"status": "failure", "message": str(e)})


# @app.route('/get_all_blogs', methods=['GET'])
# def get_all_blogs():
#     try:
#         data = request.get_json()
#         response = Blogs().get_all_blogs(data)
#         return jsonify(response)
#     except Exception as e:
#         return jsonify({"status": "failure", "message": str(e)})
#
#
#

@app.route('/get_all_blogs', methods=['GET'])
def get_all_blogs_route():
    try:
        data = request.get_json()
        # data = request.get_json()
        response = Blogs().get_all_blogs(data)
        return jsonify(response)
    except Exception as e:
        return jsonify({"status": "failure", "message": str(e)})
