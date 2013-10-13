Live Blog API Tutorial
==========================

You can send GET requests for information to a Live Blog instance without needing to authenticate first. Responses are XML format by default, and are a combination of links to more information and text surrounded by markup.

In this example we request a complete list of Blogs hosted at the demo Live Blog server, decide which one we want from the title of the Blog, and then request all of the posts from that Blog.

#. Get the list of Blogs from server::

     GET http://doc.sd-demo.sourcefabric.org/resources/LiveDesk/Blog``
   
   .. literalinclude:: examples/blog.xml
      :language: xml

#. For each of these five Blogs, follow the link for information about the blog::

     GET http://doc.sd-demo.sourcefabric.org/resources/LiveDesk/Blog/1
     GET http://doc.sd-demo.sourcefabric.org/resources/LiveDesk/Blog/2
     GET http://doc.sd-demo.sourcefabric.org/resources/LiveDesk/Blog/3
     GET http://doc.sd-demo.sourcefabric.org/resources/LiveDesk/Blog/4
     GET http://doc.sd-demo.sourcefabric.org/resources/LiveDesk/Blog/5

   Excerpt response from Blog 5:

   .. literalinclude:: examples/blog.5.xml
      :language: xml
      :lines: 1-7

   Excerpt response from Blog 4:

   .. literalinclude:: examples/blog.4.xml
      :language: xml
      :lines: 1-7

   ...
       
#. Decide that we want to get posts from "Test live blog to reproduce duplication of republished wrap-up posts", which we know is Blog 4::

      GET http://doc.sd-demo.sourcefabric.org/resources/LiveDesk/Blog/4/Post/Published

   .. literalinclude:: examples/blog.4.post.published.xml
      :language: xml
      :lines: 1-7

   Note that we are only requesting Published posts here, to get Draft posts also ommit ``/Published`` from the URL.

#. Follow each link for details of each post::

      GET http://doc.sd-demo.sourcefabric.org/resources/LiveDesk/Blog/4/Post/72

   .. literalinclude:: examples/post.72.xml 
       :language: xml

#. Complete the information about the Author, Type of Blog post, etc by following the links in the response.

See :ref:`Resources` for more information.
