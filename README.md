# Brief introduction

This project was implemented with Flask web application framework, aiming at building an e- commerce shopping website especially on electronical devices. Main features including user register, login, logout, adding items to shopping cart and wish list, ordering products, checking previous orders, browsing personal user page and so on.

# Functionality

All functionality including user register, login, logout, adding items to shopping cart and wish list, ordering products, checking previous orders, browsing personal user page, checking launch time for this website and so on.

## Register

User could register by entering their email, username and password (password length should over 8 characters), setting question (there are multiple questions available) and personal answer for resetting password purpose, and finally they should agree on privacy-policy and cookies to be stored in browsers.

## Login

User could login after their registration, if they tick the option of "remember me" during login, the cookies will be stored in browser while next time browser will automatically login for them. To be notice that there are many pages only available for login users, such as cart.html, order.html, wishlist.html, my-acount.html and so on. All these functions are decorated by "login_required" decorator.

## Login_required

a customized "login_required" decorator is defined, which will work before view function if it is wrapped by this decorator. It will check whether user's email information was stored in session, if does not, it should redirect user to log-in page.

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/1.jpg)

## Logout

After login, user could just click the top right button (next to their username) to logout.

## Cart

In the index.html page, user could add items to their cart after login.

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/2.jpg)

Another way to add items to cart is to click in product details page and choose quantities then add them to cart.

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/3.jpg)

Finally, customers could also click into their wish list, then add them to their cart.

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/4.jpg)

Cart icon will display how many types of items that user added to their cart.

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/5.jpg)

In the cart page, user could change the quantity of each item, and on the right the total money will be automatically computed, if user do not want to check right now, they could just click update cart to store these changes, or they could just check out.

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/6.jpg)

## Wish List

In the index.html page, user could add items to their wish list after login.

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/7.jpg)

Users could check and delete items in their wish list page

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/8.jpg)

## Order

After user click "checkout" button in the cart page, web system will redirect to a page that

prompt user this order is successfully created.

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/9.jpg)

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/10.jpg)

After that, user could check their orders by click the top right button (next to the cart icon), or they could wait 5 seconds to automatically redirect to order page. In the order page, the sequence is sorted by time (the latest order will be displayed firstly). In the form, order id, products quantity, total costs and time will be displayed, customers also are allowed to check particular order details by clicking the button on the right.

In the order detail page, user could browse detail order information like order id, products in detail, including their quantities and costs.

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/11.jpg)

## Personal page

After user login, they could enter their personal pages, where they could see their user id, email, question and answer for resetting the password, along with their location through Baidu Map API.

## Launch-time

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/12.jpg)

In the launch-time page, it will display that total running time for this server.

## Erro-404

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/13.jpg)

If user had accidentally type in wrong URL, error-404 page will stop them and prompt them to go back to home page.

All 404-error will be captured and return to this error page. Accordingly, logger will also record this information.

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/14.jpg)

# Web forms

When handling requests, there are a variety of fields in the web forms in this application.

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/15.jpg)

For instance, there are "email, password, number and text" type for input fields, moreover, select, checkbox and other forms were also putted into consideration during development. Web form in forget.html for resetting password:

Web form in index.html for logging in:

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/16.jpg)

Web form in cart.html to choose number for the number of products:

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/17.jpg)

By this means, validations are checked in both sever side and client side.

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/18.jpg)

For instance, in the register.html page, password length should be over 8 characters, so if user enter too short password, the web forms should not be posted in order to enhance sever proficiency, and corresponding prompts will be alerted for user to adjust their information.

Other constraints like wrong format of email address (if missing "@"), missing fields (including not agree privacy policy). In the situation above, all checks are undergoing through JavaScript, in other words, are processed in client side.

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/19.jpg)

However, if all client-side checks are passed, all web forms will also be posted to sever side, in order to carry on sever slide examination. For instance, if user posted log-in request, server- side will check whether this user (by identifying email) is existed, then check whether password is correct by querying database. Likewise, if something goes wrong, sever-side will return information to communicate with the displaying front-end, and prompt out alerts to inform user.

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/20.jpg)

If user is not existed:

If the password is wrong:

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/21.jpg)

# Database

In the web application, SQLite was chosen since the scale of the web application is relatively small, thus light-weight database is already enough.

ER diagram for database table is below:

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/22.jpg)

There are in total 9 tables. It is also clearly to see that there are a variety of filed types along with different length limitations, such as varchar (16), varchar (32), varchar (40), varchar (256), datetime, int (11), float, double, tiny text.

Table alemic_version is used for database migration, recorded previous version of migration history.

Table user is used for recording user information such as username, email, password, question and answer to reset password. The id is primary key, while cart_id and wishlist_id are foreign keys linked to cart and wishlist table.

Table cart is used for recording current user cart information, such as total money and products number in the cart. The id is primary key, while it is linked with table user by flask relationship (back-ref).

Table wishlist is used for recording current user wish list information, to be more specifically, the products number in the wish list. The id is primary key, while it is linked with table user by flask relationship (back-ref).

Table order is used for recording current user orders information, such as the time, product number and costs of each order. The id is primary key, while user_id is foreign key, it is linked with table user by flask relationship (back-ref).

Table cartdetail is used for recording current user cart specific information, such as which product, amount, and the total cost. The id is primary key, while product_id is foreign key, it is linked with table product by flask relationship (back-ref), and cart_id is also foreign key linking with table cart by flask relationship (back-ref).

Table orderdetail is used for recording current user order specific information, such as which product, amount, and the total cost. The id is primary key, while product_id is foreign key, it is linked with table product by flask relationship (back-ref), and order_id is also foreign key linking with table order by flask relationship (back-ref).

Table wishlistdetail is used for recording current user wish list specific information like which product wish list has. The id is primary key, while product_id is foreign key, it is linked with table product by flask relationship (back-ref), and wishlist_id is also foreign key linking with table wishlist by flask relationship (back-ref).

Table product is used for recording all products specific information, such as product name and unit price. The id is primary key, and it is linked with table cartdetail, wishlistdetail and orderdetail.

From the information above, we could clearly determine that the models of this web application have at "many to many" relationships. For instance, a user could have many orders, while an order could have many products, and one product could also belong to many different orders. Likewise, table cart and wish list also has similar relationship with table product.

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/23.jpg)

For the consistency between font-end and back-end, all nullable values are all required user to fill, otherwise no posts will be sent to the server-side, which means invalid data would not be stored in the database. For instance, the "email" filed is required to be unique in the database, therefore, when registering new account, checks for no identity email address will be executed to avoid fail in consistency.

For the queries when manipulating the database, function below is used to handle searching products, query will be sent to find all product name or product price that contain keyword "q" which is posted from user, then information will be returned to HTML pages to display all data. Cart, wishlist and order page has similar business logic.

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/24.jpg)

# Authentication & Sessions

In order to implement authentication & sessions, cookies and session are embedded in this web application. Cookies and Sessions are vital web technique, which allows users to have better experience manipulating the web application. Generally, cookies are log-in status and other useful information that stored in the browsers while sessions are corresponded to the server. For instance, when user ticks "remember me" option, the website will remember the user's log-in status for around entirely a month, which means once they logged in, they would not need to enter password repeatedly.

When register new account, user must agree on privacy-policy and allow this web application to use cookies, once grant their consents, the register procedure could carry on.

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/25.jpg)

"Remember me" option could store current user information to sessions, while next time

system will automatically log in for this user.

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/26.jpg)

A notice will be remained in the bottom of home page to prompt user that this website will use cookies until they agree this term.

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/27.jpg)

Once user has logged in, their "username" and "logout" button will be replaced for previous "register" and "login" button.

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/28.jpg)

After logging in, click username would redirect to personal user page, which would display basic information including user id, email, question and answer to reset their password, along with a map exhibiting their locations through HTML5 advanced features through Baidu Map API.

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/29.jpg)

For the case that of user forgetting their password, several options were considered for implementations such as user could using emails or text messages for validation to reset their passwords. However, in this project, a traditional way was adapted by user setting their question and answer to confirm their identities. Justification of this method is because this mean is relatively convenient and would not require additional services for the server-side. For instance, user should set their question (there are multiple built-in questions) and answer during registration like below:

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/30.jpg)

## Flask Template

Flask provide template engine called jinja2 along with werkzeug. Adopting this technique is mainly used to avoid code redundancy, all HTML files could inherit template with basic framework and importing relative CSS files and JavaScript scripts. In this project, two template files were created ("template.html" and "prodocut-tempalte.html", all other HTML files are inherited from these templates.

## Migrate

Migrate is vital in providing version control for previous database model. All the histories are stored in the folders of "migrations/versions", simply run the command "python manage.py db upgrade" or "python manage.py db downgrade" to execute these processes (such as upgrade or downgrade to previous version).

## g object

g object is a global namespace for app context. This is usually implemented along with the cookies and sessions. If every query retrieves data from cookies and sessions again and again would be inefficient. Therefore, after browser had sent pre-stored data to the server, global variables g object will store that information in local.

In the code below, executing sequence is defined in Flask as \@before_request =\> view function =\> contect_processor, after that a request is returned where "\@before_request" and "contect_processor" are built-in decorators just like "\@app.router" in Flask.

It is noticeable that a decorator is defined wrapping by "\@app.before_request", this decorator will execute before all the requests, to retrieve any possible storage in sessions, then will search it from the database, after that, information will be stored in g object, which could enhance server performance to avoid repeating query for cookies and sessions.

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/31.jpg)

Another decorator is created working as a hook function after every end of view function, its main purpose will check whether g object has attribute of "user", if it has, then we retrieve it and could use it after that, otherwise it will return empty value.

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/32.jpg)

## Decorator

In flask, executing sequence is defined as \@before_request =\> view function =\> context_processor. At first, user post a request to the web server, decorator \@before_request will be running, then Flask view function, finally executes context_processor.

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/33.jpg)

From the image below, "my_before_quest" decorator was created with the wrapper of "\@app.before_request", it is used to determine whether user is logged in, once the email information is founded in sessions, user information will be searched in database, and pass it to local g object.

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/34.jpg)

From the image below, "my_context_processor" was created with the wrapper of "\@app.context_processor", it is used to determine whether g object has user information (passed by "my_before_quest" function), this data would be dumped to HTML template if there is, then flask template could just use {{ g.user }}.

From the image below, a customized decorator is defined named "login_required", this function will execute before, for every view function that wrapped by this decorator. Its main function is to check whether user's email information is stored in session, if does, means this user has already logged in, otherwise it should redirect user to log-in page.

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/35.jpg)

# Styling

Displaying style in desktop for different browsers Microsoft Edge

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/36.jpg)

Google Chrome

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/37.jpg)

Displaying style in tablet for different sizes: ipad (768\*1024)

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/38.jpg)

ipad pro (1024\*1366)

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/39.jpg)

Displaying style in phones for different sizes iPhone X (375\*812)

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/40.jpg)

iPhone 5/SE (320\*568)

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/41.jpg)

In order to improve accessibility for this web application, the "alt" attribute of an image is set by tags that corresponding to the picture to help visual impaired user to obtain information. Moreover, high contrast and bright color scheme along with large font-size were designed to help most user to distinguish different areas easily. Moreover, in consideration of visual impartial people, tests of accessibility through adjusting the grayscale were carried out, ensuring achromats and color blindness patients can differentiate the image to text clearly and easily.

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/42.jpg)

# Unit Testing

Unit tests are important to ensure web application to run correctly in database query and all boundary cases.

## Postman

Postman is a collaboration testing tool for API development, it is a useful testing tool to REST, SOAP and other forms of requests easily. It is often used during collaboration where developers could just test their APIs separately.

There are 9 requests postman testing collection in total (8 post requests and 1 get request),



and there is also a file named "Buynow.postman_collectoin.json" in the "test" folder that contain all these tests provided.

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/43.jpg)

Examples test of "register":

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/44.jpg)

Examples test of "login":

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/45.jpg)

## Selenium

Selenium is a portable framework for testing web applications, which provides a playback tool for authoring functional tests for a plenty of programming language such as C\#, PHP, JAVA, Python and so on, this tool could record all the operations simulating real user visiting.

There are also 10 tests in Selenium of this project.

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/46.jpg)

It is stored in "test" folder as "Buynow.side" (using Selenium IDE to open).

> ![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/47.jpg)

## Pytest

Pytest is a framework makes it easy to write tests ranging from small tests scales to support complex functional testing for applications and libraries, it also could be used to carry on unit test for web applications.

In the folder "test/pytest", there are 10 pytest scripts used for testing.

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/48.jpg)

Example of testing for "addCart":

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/59.jpg)

## Request

Request is a python library that could send Post or Get requests, and widely used in web crawler and other fields. It could also used to carry on unit tests.

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/50.jpg)

Example of testing "search":

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/51.jpg)

## unittest

unnitest module contains a set of running test tools to carry on all tests including database query and all boundary tests.

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/52.jpg)

In the file of "test/buynow_unittest.py", define 9 tests to carry on all unit tests.

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/53.jpg)

# Logging

During the development and deployment stage, logging is vital important throughout all processes by providing useful debugging and other information in details, especially using those data to track and monitor. To achieve this, "logging" module in python was embedded, while 3 logging levels were configured as "info, warning and error" respectively.

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/55.jpg)

Noticeably, four logging handlers were set, including a logger to record all information, one info-logger only record info-level information, one warning-logger only record warning-level information and one last error-logger only record error-level information. Thus, four files will be generated as "all.log, info.log, warning.log and error.log" respectively.

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/56.jpg)

Three types of recording examples (info, warning, error)

To be more specifically, content of different files will be displayed as follow:

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/57.jpg)

It is clearly that the logger will record the time, source, logging level and which user had done something. However, if the user did not log in yet, it will record "someone", otherwise it would display username (like "DAZHA"), example is given below:

# Deployment

To gain more knowledge about building a web application, the step of deployment is indispensable. Nevertheless, the website would not require high performance server to carry on difficult computations or multiple threads requests, so Pythonanywhere as a free and python environment built-in deployment system is recommended.

The link of deployed application is bellowed: [<span class="underline">http://dazhadazha.pythonanywhere.com/</span>](http://dazhadazha.pythonanywhere.com/)

# Features

## Bootstrap & jQuery

This web application had been embedded with a variety of features, such as Bootstrap, jQuery, Some HTML5 advanced features like local storage and geolocation, AJAX and Flask-RESTful. Bootstrap is thoroughly implemented during all HTML page developing, which is an open- source web page framework which provides a variety of responsive components and layouts, while jQuery is well-built JavaScript function library which could simplify basic operation of DOM. In this project, these two technologies are both embedded into HTML, CSS and JavaScript code, to achieve responsibility of different sizes, input validator, prompt and other interactions between application and user.

## HTML5 advanced features

In this project, HTML5 advance features such as Geolocation and Local storage were embedded. In order to enhance user experience in personal customize page, Baidu Map API was implemented along with Geolocation and Local storage.

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/58.jpg)

Firstly, web application will query location of current user, once the value is obtained, they will be stored in local storage, to avoid repeatedly query for geographical information. After that, the location will be set as a marker in Baidu Map to show current user information, and also for computing shipping fees and setting default shipping address for user (this functionality presumably will be implemented in later version) because this application is aiming at providing a better user experience for user.

Prompt to query for location of user

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/59.jpg)

Data stored in local storage

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/60.jpg)

## AJAX

Ajax is short for Asynchronous JavaScript and XML, which is a set of web development techniques tools on the client side to create asynchronous web applications. By using Ajax, data can be sent and retrieved from servers asynchronously without conflicting other contents. Simply through decoupling the data between interchange layer and the presentation layer, this technique allows web pages and web applications to update content dynamically without reloading entire page. In this project, requests were designed through AJAX which aiming at enhancing user experience.

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/61.jpg)

## Redis

Redis is an open source in-memory data structure store, used as a database, cache and

message broker. It supports data structures such as strings, hashes, lists, sets and etc. It also has built-in replication, transactions and different levels of on-disk persistence. In this project, Redis is used along with Celery to implement AJAX.

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/62.jpg)

## Celery

Celery is a simple, flexible, and reliable distributed system to enormous amounts of messages, while providing operations with the tools required to maintain such a system. It also offers functionality of task queue for real-time processing, while also supporting task scheduling. In this project, Celery s is used along with Redis to implement AJAX.

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/63.jpg)

## RESTful

Representational state transfer is short for REST, which is a software architectural style with a set of constraints for Web services. Whilst RESTful means web services that observed the limitation of REST style, providing interoperability on computer systems. It also allows requests to access and manipulate textual representations of Web resources with a uniform and predefined set of stateless operations.

# Security

## CSRF

There were many cybercrimes since the invention of Internet, such as Cross-site request forgery (CSRF) and other Cross-site scripting (XSS) related security vulnerability. More importantly, directly storing or transmitting cleartext password of customer in database is also

not safe which means encryption is required during these processes. Cross-site request forgery (CSRF) is known as a common security vulnerability could be used by attackers especially for websites that using cookies and sessions to store temporary data. Hackers will forge malicious site that aims at stealing passwords, by taking advantages of vulnerable submitting forms. A secret token is introduced to this project to solve this problem within the Flask code which is automatically provided by the server when client requesting pages.

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/64.jpg)

## XSS

Cross-site scripting (XSS) threat is a method that hackers used to undermine the web system by submitting unauthorized code which let web server to run, resulting users redirecting to malicious URLs, aiming at stealing their information. Therefore, unauthorized content should be banned to return for users, while Flask templating engine (jinjia2) already activate this setting by default.

## Cookies & Sessions

Cookies, sessions and private information are also target of attackers. This project has implemented encryption by import library "werkzeug.security"

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/65.jpg)

## Database

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/66.jpg)User table for datable model is defined as follow, an initial function " init " is defined to generate password through hash method for encryption purpose, while checking password function is also defined, by carry on identical encryption process to handle requested raw password, then comparing to values stored in database, which could avoid storage of cleartext password. When view functions need to check password, they could just simply call the check function. By this means, password stored in database is encrypted, which means no cleartext passwords are stored in database.

![images](https://github.com/DAZHAdazha/BuyNow/blob/master/images/67.jpg)

## Potential risks

Some built-in modules could also consider to be embedded in order to enhance security such as Flask-security, which is an extension used in role managing and providing authentication to verify sessions and cookies.

# Version Control

In order to manage code more conveniently, version control was implemented to this project through git. To check all history commits could through Github repository below: [<span class="underline">https://github.com/DAZHAdazha/BuyNow</span>](https://github.com/DAZHAdazha/BuyNow)

# Evaluation

When designing this web application, some other functionalities were considered such as online payment procedure, including fill their shipping address and tracking their shipping order. However, since this website is only a demo, and no actual payment will be carried on, so those implementations were not realistic (though it is vital in real project). There are also plenty of more advanced techniques to be considered, such as Celery, Redis, flask-security and so on.

## Reflection

During development of this project, I had learned deployment of web application on Pythonanywhere, which deepen my understanding on web technology, and I also designed a many to many relationship using relational database, especially on setting all foreign keys

constraints. Moreover, logging was putted into consideration to track all useful information or catching warning and error happens, which is useful to enhance management experience. Additionally, unit tests were also new technology that I had implemented to this project, using Selenium, Postman and Pytest were convenient to test all functionalities on both client-side and sever-side. Finally, some advanced features like AJAX and flask-RESTful which aiming at improving user experience were also useful to learn which could save time of users and provide a smooth using experience, meanwhile enhancing sever performance. Nevertheless, there are still some challenges in developing this project. Generally speaking, Flask is a light- weight web application framework, while SQLite is also a light-weight database, there are presumably some potential issues happening when scaling up this web application. Besides, multiple threads and heavy traffic on network are also serious problems that existed in real developing for quite long time. To sum up, though Flask developing is only a small-scale framework, it still considers all aspects of real web application developments, which is quite valuable experience for me.

# Reference

Icon choice:

[<span class="underline">https://www.iconfont.cn/</span>](https://www.iconfont.cn/) 

Template choice:

[<span class="underline">http://www.bootstrapmb.com/muban</span>](http://www.bootstrapmb.com/muban) 

Baidu Map API:

 [<span class="underline">https://lbsyun.baidu.com/</span>](https://lbsyun.baidu.com/)

Deployment for Flask project on Pythonanywhere:

 [<span class="underline">https://www.jianshu.com/p/9974701034ef</span>](https://www.jianshu.com/p/9974701034ef) [<span class="underline">https://help.pythonanywhere.com/pages/Virtualenvs</span>](https://help.pythonanywhere.com/pages/Virtualenvs) 

Local storage:

[<span class="underline">https://www.runoob.com/jsref/prop-win-localstorage.html</span>](https://www.runoob.com/jsref/prop-win-localstorage.html) 

Pytest:

 [<span class="underline">https://blog.csdn.net/u012861467/article/details/100557756</span>](https://blog.csdn.net/u012861467/article/details/100557756)

Logging:

[<span class="underline">https://www.flyml.net/2018/12/12/flask-logging-usage-demo/</span>](https://www.flyml.net/2018/12/12/flask-logging-usage-demo/) 

Flask-template:

 [<span class="underline">https://blog.csdn.net/qq_33769914/article/details/109402190</span>](https://blog.csdn.net/qq_33769914/article/details/109402190) [<span class="underline">https://blog.csdn.net/qq_29286967/article/details/80948360</span>](https://blog.csdn.net/qq_29286967/article/details/80948360) 

Redis: [<span class="underline">https://blog.csdn.net/qq_38905818/article/details/104581814</span>](https://blog.csdn.net/qq_38905818/article/details/104581814) 

https://[www.runoob.com/w3cnote/python-redis-intro.html](http://www.runoob.com/w3cnote/python-redis-intro.html) 

Celery:

[<span class="underline">https://blog.miguelgrinberg.com/post/using-celery-with-flask</span>](https://blog.miguelgrinberg.com/post/using-celery-with-flask) [<span class="underline">https://docs.celeryproject.org/en/latest/userguide/monitoring.html</span>](https://docs.celeryproject.org/en/latest/userguide/monitoring.html) 

RESTful:

 [<span class="underline">https://www.cnblogs.com/donghaoblogs/p/10389696.html</span>](https://www.cnblogs.com/donghaoblogs/p/10389696.html) [<span class="underline">http://www.pythondoc.com/Flask-RESTful/quickstart.html</span>](http://www.pythondoc.com/Flask-RESTful/quickstart.html) [<span class="underline">https://blog.csdn.net/flancklin/article/details/52311505</span>](https://blog.csdn.net/flancklin/article/details/52311505)
