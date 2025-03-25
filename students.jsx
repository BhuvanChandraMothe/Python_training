const Items = ({ items }) => {
    return (
        <>
            <div>
            
                    <h1>Student Component</h1>
                    {items.length > 0 ? (
                    <table border='1'>
                        <thead>
                            <tr>
                                {Object.keys(items[0]).map((key, index) => (<th key={index}>{key}</th>))}
                            </tr>
                        </thead>
                        <tbody>
                            {items.map((items, index) => {
                                return (
                                    <tr key={index}>
                                        {Object.keys(items).map((key, index) => (
                                            <td key={index}>
                                                {Array.isArray(items[key])? (
                                                    items[key].map((mark, index) => (
                                                        <span key={index}>{mark}, </span>
                                                    ))
                                                ) : (
                                                    items[key]
                                                )}



                                            </td>

                                        ))}
                                    </tr>
                                )
                            })}
                        </tbody>
                    </table>
                    ) : (<h1>No data found</h1>)}
                
                
            </div>
        </>
    )


}
export default Items;
