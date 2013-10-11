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

   .. literalinclude:: examples/blog.xml
      :language: xml  

   :query offset: Blog offset. Integer, default 0.
   :query limit: Number of Blogs to show. Integer.
   :reqheader Authorization: Session authorization token, see :ref:`Authentication`
   :statuscode 200: Success

.. http:get:: /Blog/(int:id)

   Shows information about Blog `id`.

   **Example Request**:
  
   .. sourcecode:: http

      GET /Blog/4 HTTP/1.1
      Host: http://doc.sd-demo.sourcefabric.org/resources/LiveDesk

   **Example Response**:

   .. literalinclude:: examples/blog.4.xml
      :language: xml  



   :query offset: Blog offset. Integer, default 0.
   :query limit: Number of Blogs to show. Integer.
   :reqheader Authorization: Session authorization token.
   :statuscode 200: Success
