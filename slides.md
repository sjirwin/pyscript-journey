## PyScript and my journey to the Web

<span style="font-size:smaller">PyCon UK 2022</span>
<center>
Scott Irwin<br/>
<br/>
<img src="images/BBGEngineering_black.png"
     style="border: none; box-shadow: none; height: 100px"
     alt="Bloomberg Engineering"/><br/>
<p>&nbsp;<p>
https://sjirwin.github.io/pyscript-journey/
</center>

------

## About Me

- Bloomberg
  - Joined in 2014 as Senior engineer and manager
  - Python educator
  - Python Guild Leader since 2018
    - Co-chair since 2021
- No previous experience developing Web applications

---

# PyScript
## The Journey Inspired

------

## PyScript

- Announced at PyCon US 2022 ([video](https://www.youtube.com/watch?v=qKfkCY7cmBQ))
- Enables using Python in client-side web apps
- Built on top of
  - [Pyodide](https://pyodide.org/en/stable/)
  - [WebAssembly](https://webassembly.org/) (WASM)

------

## Some PyScript Features

- Bi-directional communication between Python and Javascript objects and namespaces
- Curated set of ready to use UI components, such as buttons, containers, text boxes
- Can use many popular Python packages
  - Including many from the scientific stack (e.g., NumPy, Pandas, Matplotlib)
  - Check [pyodide/packages](https://github.com/pyodide/pyodide/tree/main/packages) for the full list

------

## Words of Caution

- <span style="color:orangered">**Not recommended**</span> for production use
- PyScript is "very alpha" and under heavy development
- Many known issues, from usability to loading times

---

# Hello World

------

## DIY

- Create `hello.html`
- Add `<head>` section that brings in `pyscript`
``` html
<head>
 <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css"/>
 <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
</head>
```
- Add `<body>`section which includes Python code in a `<pyscript>` section
 ``` html
<body>
 <py-script>print('"Hello World!" from PyScript!!!')</py-script>
</body>
 ```

------

## DIY Result

<img src="images/hello_world_from_pyscript.png"
     style="border: none; box-shadow: none; height: 500px;"
     alt="Hello World from PyScript"/>

------

## PyScript Demos

[https://pyscript.net/examples/](https://pyscript.net/examples/)

- Hello World<br/>
<img src="images/hello_world_example.png"
     style="border: none; box-shadow: none; height: 400px;"
     alt="Hello World Example"/>

------

## PyScript Demos - REPL

``` html
<py-repl id="my-repl" auto-generate="true"> </py-repl>
````

- [example repl](https://pyscript.net/examples/repl.html)
- [example repl2](https://pyscript.net/examples/repl2.html)
<br/>
<img src="images/hello_world_repl.png"
     style="border: none; box-shadow: none; height: 400px;"
     alt="Hello World in REPL"/>

---

# Web Server

------

## place holder
