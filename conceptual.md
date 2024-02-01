### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
  open source object-relational database system that uses and extends the SQL language combined with many features that safely store and scale the most complicated data workloads.

- What is the difference between SQL and PostgreSQL?
  The PostgreSQL server is a well-known open-source database system that extends the SQL the world standard for database querying language

- In `psql`, how do you connect to a database?
  \l for databases \c DatabaseName to switch to db \df for procedures stored in particular database

- What is the difference between `HAVING` and `WHERE`?
  WHERE: Decide which rows to use
  HAVING: Determine which grouped results to keep

- What is the difference between an `INNER` and `OUTER` join?
  Inner: Only the rows that match the condition in both tables.
  Outer has two different option: Left outer and Right outer.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
  Left: All of the rows from the first table (left), combined with matching rows from the second table (right).
    
  Right: The matching rows from the first table (left), combined with all the rows from the second table (right).

- What is an ORM? What do they do?
  is a technique that lets you query and manipulate data from a database using an object-oriented paradigm. When talking about ORM, most people are referring to a library that implements the Object-Relational Mapping technique. 

  node = TreeNode('rootnode')
  node.append('node1')
  node.append('node3')
  session.add(node)
  session.commit()

  dump_tree(node)

- What are some differences between making HTTP requests using AJAX and from the server side using a library like `requests`?

  HTTP is the protocol (procedure of communication) that both the web server and the web browser understand. With both AJAX and non-AJAX the browser sends HTTP requests and receives HTTP responses from the web server.

- What is CSRF? What is the purpose of the CSRF token?
   is a unique security measure designed to protect web applications from unauthorized or malicious requests. It’s a specific type of token, often referred to as a synchronizer token or challenge token, that verifies the authenticity of requests made by a user.

- What is the purpose of `form.hidden_tag()`?
  is a template argument that creates a hidden field that contains a token. The token protects the form from CSRF attacks.