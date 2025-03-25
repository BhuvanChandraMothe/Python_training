const Item = ({ item }) => {
    return (
        <tr>
        {Object.keys(item).map((key, index) => (
            <td key={index}>
                {Array.isArray(item[key])
                    ? item[key].map((mark, index) => (<span key={index}>{mark}, </span>)) 
                    : item[key]}



            </td>

        ))}
        </tr >
    
    
    )
}

export default Item;
