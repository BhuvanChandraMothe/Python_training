import { Component } from "react";

class ParentComponent extends Component{
    render(){
        const {products} = this.props;
        return(
            <div>
                <h1> The products </h1>
               
                <table border='1' bgcolor="rosybrown">
                    <thead>
                        <tr>
                            {/* <th>Id</th>
                            <th>Name</th>
                            <th>Price</th> */}
                            {Object.keys(products[0]).map((propName, index) => (<th key={index}>{propName.toUpperCase()}</th>))}
                        </tr>
                    </thead>
                    <tbody>
                        {
                            products.map((product, index) => (
                                <tr key = {index}>
                                    {Object.keys(product).map((propName, index) => (
                                        <td key = {index} > {product[propName]}</td>
                                    ))}
                                </tr>

                                
                            ))
                        }
                    </tbody>
                </table>
            
            </div>
                )
        
    }
}

export default ParentComponent;
