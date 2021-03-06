from flask import Blueprint, render_template, abort, current_app, session, request, Markup


from db import database_wrapper

import query	
import markdown

class BlogCMS(object):
	def __init__(self):
		pass


	def timeline(self, content_db):
		posts = query.getAllPosts(content_db)


		if posts:
			posts = {post_id: data for post_id, data in posts.iteritems() if data["post_published"] == 1}

			for post_id, data in posts.iteritems():

				post_content = data.get("post_content", None)

				if post_content:
					post_content = post_content.replace('<br />', '\n')
					data["post_content"] = markdown.markdown(post_content, extensions=['markdown.extensions.fenced_code', 'markdown.extensions.nl2br'])

				else:
					posts[post_id]["post_content"] = ""
		else:
			posts = None
		

		return render_template("/timeline.html", posts = posts)


	def get_post_content(self, content_db, post_id):
		post = query.getPost(content_db, post_id)
		return post

	def get_post_content_by_handle(self, content_db, post_handle):
		post = query.getPostByHandle(content_db, post_handle)
		return post