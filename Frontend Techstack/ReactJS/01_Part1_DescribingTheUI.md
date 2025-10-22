React is JS library for rendering UI 

Overview (Part 1)
How to write your first React component
When and how to create multi-component files
How to add markup to JavaScript with JSX
How to use curly braces with JSX to access JavaScript functionality from your components
How to configure components with props

---

How to write your first React component

React applications are built from isolated pieces of UI called components. 

A React component is a JavaScript function that you can sprinkle with markup. Components can be as small as a button, or as large as an entire page. 

“components”, reusable UI elements for your app

Here is a Gallery component rendering three Profile components:

function Profile() {
  return (
    <img
      src="https://i.imgur.com/MK3eW3As.jpg"
      alt="Katherine Johnson"
    />
  );
}

export default function Gallery() {
  return (
    <section>
      <h1>Amazing scientists</h1>
      <Profile />
      <Profile />
      <Profile />
    </section>
  );
}

Export default - stamndard js syntax lets you mark the main function in a file so that you can later import it from other files

Define the function - With function Profile() { } you define a JavaScript function with the name Profile (Note always start wityh capital letter!)

Add markup
return (
  <div>
    <img src="https://i.imgur.com/MK3eW3As.jpg" alt="Katherine Johnson" />
  </div>
);

Nesting components 
As u have defined profile component, you can also nest it in another compoents - export a gallery componet that uses multiple profile components 

You can also move Profile to a seperate fle if the file gets crowded. (in the section of page about imports ahead)

Gallery is a parent component, rendering each Profile as a “child”

NOTE!
Components can render other components, but you must never nest their definitions:

export default function Gallery() {
  // 🔴 Never define a component inside another component!
  function Profile() {
    // ...
  }
  // ...
}
The snippet above is very slow and causes bugs. Instead, define every component at the top level:

export default function Gallery() {
  // ...
}

// ✅ Declare components at the top level
function Profile() {
  // ...
}
When a child component needs some data from a parent, pass it by props instead of nesting definitions.

---

When and how to create multi-component files

Importing and Exporting Components

What if you want to change the landing screen in the future and put a list of science books there? Or place all the profiles somewhere else? It makes sense to move Gallery and Profile out of the root component file. This will make them more modular and reusable in other files. You can move a component in three steps:

Make a new JS file to put the components in.
Export your function component from that file (using either default or named exports).
Import it in the file where you’ll use the component (using the corresponding technique for importing default or named exports).

Here both Profile and Gallery have been moved out of App.js into a new file called Gallery.js. Now you can change App.js to import Gallery from Gallery.js:

App.js
import Gallery from './Gallery.js';

export default function App() {
  return (
    <Gallery />
  );
}


Gallery.js
function Profile() {
  return (
    <img
      src="https://i.imgur.com/QIrZWGIs.jpg"
      alt="Alan L. Hart"
    />
  );
}

export default function Gallery() {
  return (
    <section>
      <h1>Amazing scientists</h1>
      <Profile />
      <Profile />
      <Profile />
    </section>
  );
}

Gallery.js:
Defines the Profile component which is only used within the same file and is not exported.
Exports the Gallery component as a default export.
App.js:
Imports Gallery as a default import from Gallery.js.
Exports the root App component as a default export.

---

Default vs Named Exports 

There are two primary ways to export values with JavaScript: default exports and named exports. 

A file can have no more than one default export, but it can have as many named exports as you like.

img 1

Method to import and export default and named
Note:  file can only have one default export, but it can have numerous named exports!

img 2


First, export Profile from Gallery.js using a named export (no default keyword):

export function Profile() {
  // ...
}
Then, import Profile from Gallery.js to App.js using a named import (with the curly braces):

import { Profile } from './Gallery.js';
Finally, render <Profile /> from the App component:

export default function App() {
  return <Profile />;
}
Now Gallery.js contains two exports: a default Gallery export, and a named Profile export. App.js imports both of them. Try editing <Profile /> to <Gallery /> and back in this example:

App.js
import Gallery from './Gallery.js';
import { Profile } from './Gallery.js';

export default function App() {
  return (
    <Profile />
  );
}


Gallery.js
export function Profile() {
  return (
    <img
      src="https://i.imgur.com/QIrZWGIs.jpg"
      alt="Alan L. Hart"
    />
  );
}

export default function Gallery() {
  return (
    <section>
      <h1>Amazing scientists</h1>
      <Profile />
      <Profile />
      <Profile />
    </section>
  );
}

Now you’re using a mix of default and named exports:

Gallery.js:
Exports the Profile component as a named export called Profile.
Exports the Gallery component as a default export.
App.js:
Imports Profile as a named import called Profile from Gallery.js.
Imports Gallery as a default import from Gallery.js.
Exports the root App component as a default export.

---

How to add markup to JavaScript with JSX - Writing markup with JSX

JSX is a syntax extension for JavaScript that lets you write HTML-like markup inside a JavaScript file.

Each React component is a JavaScript function that may contain some markup that React renders into the browser. React components use a syntax extension called JSX to represent that markup. JSX looks a lot like HTML, but it is a bit stricter and can display dynamic information. 

The Rules of JSX 

1. Return a single root element 

To return multiple elements from a component, wrap them with a single parent tag.

For example, you can use a <div>:

<div>
  <h1>Hedy Lamarr's Todos</h1>
  <img 
    src="https://i.imgur.com/yXOvdOSs.jpg" 
    alt="Hedy Lamarr" 
    class="photo"
  >
  <ul>
    ...
  </ul>
</div>
If you don’t want to add an extra <div> to your markup, you can write <> and </> instead:

<>
  <h1>Hedy Lamarr's Todos</h1>
  <img 
    src="https://i.imgur.com/yXOvdOSs.jpg" 
    alt="Hedy Lamarr" 
    class="photo"
  >
  <ul>
    ...
  </ul>
</>
This empty tag is called a Fragment. Fragments let you group things without leaving any trace in the browser HTML tree.

2. Close all the tags 

3.  camelCase all most of the things! 
For example, instead of stroke-width you use strokeWidth. Since class is a reserved word, in React you write className instead, named after the corresponding DOM property

Error messages will often point you in the right direction to fixing your markup.

---

How to use curly braces with JSX to access JavaScript functionality from your components

JSX lets you write HTML-like markup inside a JavaScript file, keeping rendering logic and content in the same place. Sometimes you will want to add a little JavaScript logic or reference a dynamic property inside that markup. In this situation, you can use curly braces in your JSX to open a window to JavaScript.

Passing strings with quotes

export default function Avatar() {
  return (
    <img
      className="avatar"
      src="https://i.imgur.com/7vQD0fPs.jpg"
      alt="Gregorio Y. Zara"
    />
  );
}

Here, "https://i.imgur.com/7vQD0fPs.jpg" and "Gregorio Y. Zara" are being passed as strings.

But what if you want to dynamically specify the src or alt text? You could use a value from JavaScript by replacing " and " with { and }:

export default function Avatar() {
  const avatar = 'https://i.imgur.com/7vQD0fPs.jpg';
  const description = 'Gregorio Y. Zara';
  return (
    <img
      className="avatar"
      src={avatar}
      alt={description}
    />
  );
}

JSX is a special way of writing JavaScript. That means it’s possible to use JavaScript inside it—with curly braces { }.


Using “double curlies”: CSS and other objects in JSX 

In addition to strings, numbers, and other JavaScript expressions, you can even pass objects in JSX. Objects are also denoted with curly braces, like { name: "Hedy Lamarr", inventions: 5 }. Therefore, to pass a JS object in JSX, you must wrap the object in another pair of curly braces: person={{ name: "Hedy Lamarr", inventions: 5 }}.

App.js

export default function TodoList() {
  return (
    <ul style={{
      backgroundColor: 'black',
      color: 'pink'
    }}>
      <li>Improve the videophone</li>
      <li>Prepare aeronautics lectures</li>
      <li>Work on the alcohol-fuelled engine</li>
    </ul>
  );
}

The next time you see {{ and }} in JSX, know that it’s nothing more than an object inside the JSX curlies!

Note: Inline style properties are written in camelCase!

---

How to configure components with props

Passing props to a component

React components use props to communicate with each other. Every parent component can pass some information to its child components by giving them props.

Familiar props 

Props are the information that you pass to a JSX tag. For example, className, src, alt, width, and height are some of the props you can pass to an <img>:

function Avatar() {
  return (
    <img
      className="avatar"
      src="https://i.imgur.com/1bX5QH6.jpg"
      alt="Lin Lanying"
      width={100}
      height={100}
    />
  );
}

export default function Profile() {
  return (
    <Avatar />
  );
}

Passing props to a component 

In this code, the Profile component isn’t passing any props to its child component, Avatar

You can give Avatar some props in 2 steps 

Step 1 : Pass props to the child component

First, pass some props to Avatar. For example, let’s pass two props: person (an object), and size (a number):

export default function Profile() {
  return (
    <Avatar
      person={{ name: 'Lin Lanying', imageId: '1bX5QH6' }}
      size={100}
    />
  );
}
Note: If double curly braces after person= confuse you, recall they’re merely an object inside the JSX curlies.

Step 2: Read props inside the child component 

You can read these props by listing their names person, size separated by the commas inside ({ and }) directly after function Avatar. This lets you use them inside the Avatar code, like you would with a variable.

function Avatar({ person, size }) {
  // person and size are available here
}

Example

App.js
import { getImageUrl } from './utils.js';

function Avatar({ person, size }) {
  return (
    <img
      className="avatar"
      src={getImageUrl(person)}
      alt={person.name}
      width={size}
      height={size}
    />
  );
}

export default function Profile() {
  return (
    <div>
      <Avatar
        size={100}
        person={{ 
          name: 'Katsuko Saruhashi', 
          imageId: 'YfeOqp2'
        }}
      />
      <Avatar
        size={80}
        person={{
          name: 'Aklilu Lemma', 
          imageId: 'OKS67lh'
        }}
      />
      <Avatar
        size={50}
        person={{ 
          name: 'Lin Lanying',
          imageId: '1bX5QH6'
        }}
      />
    </div>
  );
}

utils.js
export function getImageUrl(person, size = 's') {
  return (
    'https://i.imgur.com/' +
    person.imageId +
    size +
    '.jpg'
  );
}

Props let you think about parent and child components independently. For example, you can change the person or the size props inside Profile without having to think about how Avatar uses them. Similarly, you can change how the Avatar uses these props, without looking at the Profile.

You can think of props like “knobs” that you can adjust. They serve the same role as arguments serve for functions—in fact, props are the only argument to your component! React component functions accept a single argument, a props object:

function Avatar(props) {
  let person = props.person;
  let size = props.size;
  // ...
}

Note: Don’t miss the pair of { and } curlies inside of ( and ) when declaring props:

function Avatar({ person, size }) {
  // ...
}


Specifying a default value for a prop 

If you want to give a prop a default value to fall back on when no value is specified, you can do it with the destructuring by putting = and the default value right after the parameter:

function Avatar({ person, size = 100 }) {
  // ...
}

Passing JSX as children (IMPORTANT)

Let’s break this down step by step 👇

### 🧩 Concept: Passing JSX as **children**

In React, **JSX elements can be nested** inside other JSX elements.
Example with HTML tags:

```jsx
<div>
  <img />
</div>
```

Here, `<img />` is **inside** `<div>`. So the `<div>` is the **parent**, and `<img>` is the **child**.

### 💡 Extending the same to custom components

You can also nest **your own React components** the same way:

```jsx
<Card>
  <Avatar />
</Card>
```

Here:

* `<Card>` is your custom parent component.
* `<Avatar />` is the nested child JSX element.

### 🧠 What happens behind the scenes

When you pass elements **inside** another component like this,
React automatically gives the parent a **special prop called `children`**.

So this:

```jsx
<Card>
  <Avatar />
</Card>
```

is the same as writing:

```jsx
<Card children={<Avatar />} />
```

That means, in the `Card` component, you can **access whatever was passed inside it** using the `children` prop.

### ⚙️ How it works in your example

**Card.js (in your App.js):**

```jsx
function Card({ children }) {
  return (
    <div className="card">
      {children}
    </div>
  );
}
```

Explanation:

* `Card` receives `{ children }` as props.
* `children` will be whatever is written **between** `<Card>` and `</Card>` in JSX.
* It then renders a `<div>` that contains `{children}`.

So when your `Profile()` returns:

```jsx
<Card>
  <Avatar ... />
</Card>
```

The `children` prop of `Card` = `<Avatar ... />`.

Hence, the final output is:

```html
<div class="card">
  <img ... />
</div>
```

---

### 🧱 File-by-file breakdown

**1️⃣ App.js**

```jsx
import Avatar from './Avatar.js';

function Card({ children }) {
  return <div className="card">{children}</div>;
}

export default function Profile() {
  return (
    <Card>
      <Avatar
        size={100}
        person={{ name: 'Katsuko Saruhashi', imageId: 'YfeOqp2' }}
      />
    </Card>
  );
}
```

* `<Card>` wraps around `<Avatar>`.
* So `<Avatar>` becomes the `children` of `<Card>`.


**2️⃣ Avatar.js**

```jsx
import { getImageUrl } from './utils.js';

export default function Avatar({ person, size }) {
  return (
    <img
      className="avatar"
      src={getImageUrl(person)}
      alt={person.name}
      width={size}
      height={size}
    />
  );
}
```

* This component just returns an `<img>` tag with the given props.


**3️⃣ utils.js**

```jsx
export function getImageUrl(person, size = 's') {
  return 'https://i.imgur.com/' + person.imageId + size + '.jpg';
}
```

* Generates the URL of the image dynamically.


### 🪞 Final Rendered Output

After everything runs, your `Profile` component renders:

```html
<div class="card">
  <img
    class="avatar"
    src="https://i.imgur.com/YfeOqp2s.jpg"
    alt="Katsuko Saruhashi"
    width="100"
    height="100"
  />
</div>
```


### ⚡ Key Takeaways

| Concept           | Meaning                                                                                                                |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **children prop** | A special prop automatically provided when you nest JSX inside a component                                             |
| **Use case**      | Lets you create *wrapper* or *layout* components (like `Card`, `Modal`, `Container`, etc.) that can wrap any child JSX |
| **Benefit**       | Makes components reusable — `Card` can wrap anything (`<Avatar>`, `<Post>`, `<Button>`, etc.)                          |


### 🌱 Bonus Tip

If you add more elements inside `<Card>`:

```jsx
<Card>
  <h2>Profile</h2>
  <Avatar ... />
  <button>Follow</button>
</Card>
```

Then `children` will be **an array of all three elements**:

```jsx
[
  <h2>Profile</h2>,
  <Avatar ... />,
  <button>Follow</button>
]
```

React will render all of them inside the `<div className="card">`.

