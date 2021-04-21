import React from "react";
import { Button, ButtonGroup, Dropdown, DropdownButton } from "react-bootstrap";
import { Link } from "react-router-dom";
import { axios } from 'axios';

const Categories = (categories) => {

  async function getProductsByCategory(id) {
    const { data } = await axios.get(`/products/?categories=${id}/`);
    console.log(data.results[0])
    return(data.results[0]);
  }

  return (
      <menu>
      {/* {console.log(categories.categories)} */}
      {categories.categories.map(category => (
        <div id={category.id}>
        <Link to={`/`}>{category.name}</Link>
      </div>
      ))}
     
    </menu>
  );
};

export default Categories;







