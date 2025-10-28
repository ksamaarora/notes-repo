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