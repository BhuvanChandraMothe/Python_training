import * as React from 'react';
import Box from '@mui/material/Box';
import { DataGrid } from '@mui/x-data-grid';


export default class DataGridDemo extends React.Component {
    constructor() {
        super();
        this.state = {
            rows: [ ],
            columns: [ ]
        }
    }
    async componentDidMount() {
        let response = await fetch('https://jsonplaceholder.typicode.com/posts');
        let data = await response.json();
        this.setState({rows : await data});
        
        Object.keys(this.state.rows[0]).map((propName) => 
            this.setState((prevState) => ({
                columns: [...prevState.columns, {field: propName, headerName: propName.toLocaleUpperCase(), width: 150, editable: true},],
            })));

    }
    render(){
        const {rows, columns} = this.state;
        return (
            <Box sx={{ height: 400, width: '100%' }}>
                <DataGrid
                    rows={this.state.rows}
                    columns={columns}
                    initialState={{
                        pagination: {
                            paginationModel:{
                            pageSize: 5,}
                        },
                    }}
                    pageSizeOptions={[5]}
                    checkboxSelection
                    disableRowSelectionOnClick
                />
            </Box>
        );
    }

}
