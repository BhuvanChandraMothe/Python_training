
import Items from "./students";





const App = () => {
  let arr = [1,2,3,4,5,6];
  let obj = {id: 1, name: 'Bhuvan', age: 20, marks: [100, 99, 98, 97, 96]};
  let students = [{id: 1, name: 'Bhuvan', age: 20, marks: [100, 99, 98, 97, 96]},
    {id: 2, name: 'Chandra', age: 21, marks: [100, 99, 98, 97, 96]},
    {id: 3, name: 'Bhuvan Chandra', age: 22, marks: [100, 99, 98, 97, 96]}];

  let products = [{id:1, Category: 'Electronics', name: 'Mobile', price: 10000},
  {id:2, Category: 'Electronics', name: 'Laptop', price: 50000},
  {id:3, Category: 'Electronics', name: 'Tablet', price: 20000},
  {id:4, Category: 'Electronics', name: 'Smart Watch', price: 5000},
  {id:5, Category: 'Electronics', name: 'Headphones', price: 1000},
  {id:6, Category: 'Electronics', name: 'Earphones', price: 500}];

  let dummy = [];
  return (
    <>
    <div>
      <h1>App Component</h1>
      <ul>
        {arr.map((val, index) => <li key = {index}>{val}</li>)}
      </ul>
    </div>
    <div>
      <h1> Object iteration</h1>
      <ul>
        {Object.keys(obj).map((key, index) => <li key={index}>{key} : {obj[key]}</li>)}
      </ul>
    </div>
    <div>

    </div>



    <Items items={students}/>
    <Items items={products}/>
    <Items items = {dummy}/>
    </>
    
  )
  
} 

export default App;
