Got it! I’ve added a clickable table of contents that jumps to each section, and kept everything else the same (just formatting). You can paste this straight into your README.

---

# React is a JS library for rendering UI

## 📘 Overview (Part 1)

* [How to write your first React component](#how-to-write-your-first-react-component)
* [When and how to create multi-component files](#when-and-how-to-create-multi-component-files)
* [How to add markup to JavaScript with JSX](#how-to-add-markup-to-javascript-with-jsx)
* [How to use curly braces { } with JSX](#how-to-use-curly-braces--with-jsx)
* [How to configure components with props](#how-to-configure-components-with-props)
* [Passing JSX as children (Important)](#passing-jsx-as-children-important)

---

## 🧩 How to write your first React component

React applications are built from isolated pieces of UI called **components**.

A React component is a JavaScript function that you can sprinkle with markup. Components can be as small as a button, or as large as an entire page.

Here is a `Gallery` component rendering three `Profile` components:

```jsx
function Profile() {
  return (
    <img
      src="https://i.r.com/MK3eW3As.jpg"
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
```

`export default` — standard JS syntax that lets you mark the main function in a file so you can later import it from other files.

### Define the function

With `function Profile() { }` you define a JavaScript function with the name **Profile** (Note: always start with a capital letter!).

### Add markup

```jsx
return (
  <div>
    <img src="https://i.imgur.com/MK3eW3As.jpg" alt="Katherine Johnson" />
  </div>
);
```

### Nesting components

As you have defined `Profile`, you can also nest it in another component and export a `Gallery` component that uses multiple `Profile` components.

You can also move `Profile` to a separate file if the file gets crowded.
`Gallery` is a **parent** component, rendering each `Profile` as a “child”.

---

### ⚠️ NOTE!

Components can render other components, but you must **never** nest their definitions:

```jsx
export default function Gallery() {
  // 🔴 Never define a component inside another component!
  function Profile() {
    // ...
  }
  // ...
}
```

The snippet above is very slow and causes bugs.
Instead, define every component at the **top level**:

```jsx
export default function Gallery() {
  // ...
}

// ✅ Declare components at the top level
function Profile() {
  // ...
}
```

When a child component needs some data from a parent, pass it by **props** instead of nesting definitions.

---

## When and how to create multi-component files

### Importing and Exporting Components

If you want to reuse components elsewhere, move them into separate files.

Steps:

1. Make a new JS file.
2. Export your component (default or named).
3. Import it where needed.

**Example**

`App.js`

```jsx
import Gallery from './Gallery.js';

export default function App() {
  return (
    <Gallery />
  );
}
```

`Gallery.js`

```jsx
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
```

**Explanation**

* `Gallery.js`: Defines the `Profile` component (not exported) and exports `Gallery` as **default**.
* `App.js`: Imports `Gallery` as a **default import**.

---

## 🔄 Default vs Named Exports

There are two primary ways to export values with JavaScript: default exports and named exports.
A file can have **only one default export**, but can have **multiple named exports**.

### Example 1 – Named export

```jsx
// Gallery.js
export function Profile() {
  // ...
}
```

```jsx
// App.js
import { Profile } from './Gallery.js';

export default function App() {
  return <Profile />;
}
```

### Example 2 – Mixing default + named exports

`App.js`

```jsx
import Gallery from './Gallery.js';
import { Profile } from './Gallery.js';

export default function App() {
  return (
    <Profile />
  );
}
```

`Gallery.js`

```jsx
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
```

---

## 🧱 How to add markup to JavaScript with JSX

JSX is a syntax extension for JavaScript that lets you write **HTML-like markup** inside JS.
JSX is a syntax extension for JavaScript that lets you write HTML-like markup inside a JavaScript file.

Each React component is a JavaScript function that may contain some markup that React renders into the browser. React components use a syntax extension called JSX to represent that markup. JSX looks a lot like HTML, but it is a bit stricter and can display dynamic information.

### The Rules of JSX

#### 1️⃣ Return a single root element

Wrap multiple elements with one parent tag:

```jsx
<div>
  <h1>Hedy Lamarr's Todos</h1>
  <img 
    src="https://i.imgur.com/yXOvdOSs.jpg" 
    alt="Hedy Lamarr" 
    className="photo"
  />
  <ul>...</ul>
</div>
```

If you don’t want an extra `<div>`, use **Fragments**:

```jsx
<>
  <h1>Hedy Lamarr's Todos</h1>
  <img 
    src="https://i.imgur.com/yXOvdOSs.jpg" 
    alt="Hedy Lamarr" 
    className="photo"
  />
  <ul>...</ul>
</>
```

#### 2️⃣ Close all tags

#### 3️⃣ Use camelCase for most attributes

`className`, `strokeWidth`, etc.

---

## 🌀 How to use curly braces { } with JSX

Sometimes you need to insert JavaScript logic inside markup — use `{ }`.
Sometimes you will want to add a little JavaScript logic or reference a dynamic property inside that markup. In this situation, you can use curly braces in your JSX to open a window to JavaScript.

### Passing strings with quotes

```jsx
export default function Avatar() {
  return (
    <img
      className="avatar"
      src="https://i.imgur.com/7vQD0fPs.jpg"
      alt="Gregorio Y. Zara"
    />
  );
}
```

### Dynamically specify values

```jsx
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
```

### “Double curlies” for inline CSS or objects

```jsx
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
```

The next time you see `{{` and `}}` in JSX, know that it’s nothing more than an object inside the JSX curlies!

> **Note:** Inline style properties are written in camelCase!

---

## ⚙️ How to configure components with props

### Passing props to a component

Props are the information you pass to a JSX tag. React components use props to communicate with each other. Every parent component can pass some information to its child components by giving them props.

**Familiar props**

Props are the information that you pass to a JSX tag. For example, `className`, `src`, `alt`, `width`, and `height` are some of the props you can pass to an `<img>`:

```jsx
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
  return <Avatar />;
}
```

### Step 1 – Pass props

```jsx
export default function Profile() {
  return (
    <Avatar
      person={{ name: 'Lin Lanying', imageId: '1bX5QH6' }}
      size={100}
    />
  );
}
```

### Step 2 – Read props

```jsx
function Avatar({ person, size }) {
  // use person and size
}
```

### Full example

`App.js`

```jsx
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
      <Avatar size={100} person={{ name: 'Katsuko Saruhashi', imageId: 'YfeOqp2' }} />
      <Avatar size={80}  person={{ name: 'Aklilu Lemma', imageId: 'OKS67lh' }} />
      <Avatar size={50}  person={{ name: 'Lin Lanying',  imageId: '1bX5QH6' }} />
    </div>
  );
}
```

`utils.js`

```jsx
export function getImageUrl(person, size = 's') {
  return (
    'https://i.imgur.com/' +
    person.imageId +
    size +
    '.jpg'
  );
}
```

---

### Setting default prop values

```jsx
function Avatar({ person, size = 100 }) {
  // ...
}
```

---

## 🎁 Passing JSX as children (**Important**)

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
