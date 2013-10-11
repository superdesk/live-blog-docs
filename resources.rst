Resources
====================

Some of the Live Blog resources.

Blogs
--------

Return information about Blogs.

.. http:get:: /Blog
   
   Lists available blogs.

   **Example Request**:
  
   .. sourcecode:: http

      GET /Blog HTTP/1.1
      Host: http://doc.sd-demo.sourcefabric.org/resources/LiveDesk

   **Example Response**:

   .. sourcecode:: xml

	<BlogList total="5" limit="5" offset="0">
		<Blog href="http://doc.sd-demo.sourcefabric.org/resources/LiveDesk/Blog/1"/>
		<Blog href="http://doc.sd-demo.sourcefabric.org/resources/LiveDesk/Blog/2"/>
		<Blog href="http://doc.sd-demo.sourcefabric.org/resources/LiveDesk/Blog/3"/>
		<Blog href="http://doc.sd-demo.sourcefabric.org/resources/LiveDesk/Blog/4"/>
		<Blog href="http://doc.sd-demo.sourcefabric.org/resources/LiveDesk/Blog/5"/>
	</BlogList>


   :query offset: Blog offset. Integer, default 0.
   :query limit: Number of Blogs to show. Integer.
   :reqheader Authorization: Session authorization token.
   :statuscode 200: Success

.. http:get:: /Blog/(int:id)

   Shows information about Blog `id`.

   **Example Request**:
  
   .. sourcecode:: http

      GET /Blog/4 HTTP/1.1
      Host: http://doc.sd-demo.sourcefabric.org/resources/LiveDesk

   **Example Response**:

   .. sourcecode:: xml



   :query offset: Blog offset. Integer, default 0.
   :query limit: Number of Blogs to show. Integer.
   :reqheader Authorization: Session authorization token.
   :statuscode 200: Success
