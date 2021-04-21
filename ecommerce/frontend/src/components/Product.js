import axios from "axios";
import React from "react";
import { Card } from "react-bootstrap";
import Rating from './Rating'
import { Link } from "react-router-dom";
import { useState, useEffect, useAsync } from "react";
import { listProductDetails } from "../actions/productActions";
import { useDispatch, useSelector } from "react-redux";
import { productImages } from "../actions/productActions";
import Categories from './Categories';

function Product({ product }) {
  const dispatch = useDispatch();
  const productImages2 = useSelector((state) => state.productImages);
  const { loading, error, images } = productImages2;
  const [imageUrl, setImageUrl] = useState("");


  return (
    <Card className="my-3 p-3 rounded">
      <Link to={`/product/${product.id}`}>
        {/* /{console.log(images)} */}
        <Card.Img src={product.image} />
      </Link>

      <Card.Body>
        <Link to={`/product/${product.id}`}>
          <Card.Title as="div">
            <strong>{product.name}</strong>
          </Card.Title>
        </Link>

        <Card.Text as="div">
                    <div className="my-3">
                        <Rating value={product.raiting} color={'#f8e825'} />
                    </div>
        </Card.Text>
  
        <Card.Text as="h3">${product.price}</Card.Text>
      </Card.Body>
    </Card>
  );
}

export default Product;
