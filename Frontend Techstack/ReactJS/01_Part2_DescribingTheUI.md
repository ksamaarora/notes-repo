Part 2 
Overview

* [How to conditionally render components](#how-to-conditionally-render-components)
* [How to render multiple components at a time](#how-to-render-multiple-components-at-a-time)
* [How to avoid confusing bugs by keeping components pure](#how-to-avoid-confusing-bugs-by-keeping-components-pure)
* [Why understanding your UI as trees is useful](#why-understanding-your-ui-as-trees-is-useful)

> How to conditionally render components

In React, you can conditionally render components based on certain conditions using JavaScript's conditional statements. Here are a few common methods to achieve this:

1. **Using `if` statements**:
```jsx
function Item({name, isPacked}) {
    if(isPacked){
        return <li className="item" >{name}</li>;
    }
    return <li className="item" >{name} (need to pack)</li>;
}
    
export default function PackingList() {
    return (
        <section>
            <h1>My Packing List</h1>
            <ul>
                <Item isPacked={true} name="Passport" />
                <Item isPacked={true} name="Socks" />
                <Item isPacked={false} name="Charger" />
            </ul>
        </section>
    );
}
```

2. **Using the ternary operator**:
```jsx
function Item({name, isPacked}) {
    return (
        <li className="item" >
            {name} {isPacked ? "" : "(need to pack)"}
        </li>
    );
}
```

3. **Using logical `&&` operator**:
```jsx
function Item({name, isPacked}) {
    return (
        <li className="item" >
            {name} {!isPacked && "(need to pack)"}
            // you can read this as "if not isPacked, then show (need to pack)"
        </li>
    );
}
```

4. Conditionally assigning JSX to variables:
```jsx
function Item({name, isPacked}) {
    let status;
    if(isPacked){
        status = "";
    } else {
        status = "(need to pack)";
    }

    return (
        <li className="item" >
            {name} {status}
        </li>
    );
}
```