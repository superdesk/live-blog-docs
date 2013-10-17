.. _Resources:

Resources
====================

.. |params| replace:: Get a complete list of parameters by adding ``&params=show`` to your request.

.. http:get:: /resources

   See a complete list of resources available on the server.

   **Example Request**:
  
   .. sourcecode:: http

      GET /resources HTTP/1.1
      Host: http://doc.sd-demo.sourcefabric.org

   **Example Response**:

   .. literalinclude:: examples/resources.xml
      :language: xml  

Blogs
--------

Resources related to Blogs.

.. http:get:: /resources/LiveDesk/Blog
   
   Lists available blogs.

   **Example Request**:
  
   .. sourcecode:: http

      GET /resources/LiveDesk/Blog HTTP/1.1
      Host: http://doc.sd-demo.sourcefabric.org

   **Example Response**:

   .. literalinclude:: examples/blog.xml
      :language: xml  

   |params|

.. http:get:: /resources/HR/User/(int:id)/Blog

   Lists blogs assigned to user `id`.

   **Example Request**:
  
   .. sourcecode:: http

      GET /resources/HR/User/5/Blog HTTP/1.1
      Host: http://doc.sd-demo.sourcefabric.org

   **Example Response**:

   .. literalinclude:: examples/user.blog.xml
      :language: xml  

   |params|

.. http:get:: /resources/HR/User/(int:id)/Blog/Live

   Lists live blogs assigned to user `id`.

   **Example Request**:
  
   .. sourcecode:: http

      GET /resources/HR/User/5/Blog/Live HTTP/1.1
      Host: http://doc.sd-demo.sourcefabric.org

   **Example Response**:

   .. literalinclude:: examples/user.blog.live.xml
      :language: xml  

   |params|

.. http:get:: /resources/LiveDesk/Blog/(int:id)

   Shows information about Blog `id`.

   **Example Request**:
  
   .. sourcecode:: http

      GET /resources/LiveDesk/Blog/4 HTTP/1.1
      Host: http://doc.sd-demo.sourcefabric.org

   **Example Response**:

   .. literalinclude:: examples/blog.4.xml
      :language: xml  

   |params|

Posts
--------------------------


.. http:get:: /resources/LiveDesk/Blog/(int:id)/Post/Published

   Shows all published posts on Blog `id`.

   **Example Request**:
  
   .. sourcecode:: http

      GET /resources/LiveDesk/Blog/4/Post/Published HTTP/1.1
      Host: http://doc.sd-demo.sourcefabric.org

   **Example Response**:

   .. literalinclude:: examples/blog.4.post.published.xml
      :language: xml  

   |params|

.. http:post:: /resources/LiveDesk/Blog/(int:id)/Post

   Insert a post into Blog `id`, but do not publish it.

   **Example Request**:
  
   .. sourcecode:: http

      POST /resources/LiveDesk/Blog/4/Post/ HTTP/1.1
      Host: http://doc.sd-demo.sourcefabric.org

   :reqheader Authorization: Session authorization token, see :ref:`Authentication`

.. http:post:: /resources/LiveDesk/Blog/(int:id)/Post/Publish

   Insert a post into Blog `id` and publish it immediately.

   **Example Request**:
  
   .. sourcecode:: http

      POST /resources/LiveDesk/Blog/4/Post/ HTTP/1.1
      Host: http://doc.sd-demo.sourcefabric.org

   :reqheader Authorization: Session authorization token, see :ref:`Authentication`

Users
------------------------------

.. http:get:: /resources/HR/User/(int:id)

   Show information about user `id`.

   **Example Request**:
  
   .. sourcecode:: http

      GET /resources/HR/User/5 HTTP/1.1
      Host: http://doc.sd-demo.sourcefabric.org

   **Example Response**:

   .. literalinclude:: examples/user.5.xml
      :language: xml  

   |params|
