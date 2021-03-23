import React, { useEffect, useState } from "react";
import { Row, Col } from "react-bootstrap";
import Product from "../components/Product";
import axios from "axios";
import { listProducts } from '../actions/productActions';
import Loader from '../components/Loader';
import Message from '../components/Message';
import { useDispatch, useSelector } from 'react-redux';
import Header from "../components/Header";
import Footer from '../components/Footer';


const HomePage = () => {
  //  const [products, setProducts] = useState([]);
  const dispatch = useDispatch();
  const productList = useSelector((state) => state.productList);
  const { error, loading, products} = productList;

  useEffect(() => {
    // async function fetchProducts() {
    //   const { data } = await axios.get("/products");
    //   //console.log(data.results)
    //   setProducts(data.results);
    // }
    // fetchProducts();

    dispatch(listProducts())

  }, [dispatch]);

  return (
    <div>
      <Header />
      <h1>{ ' '}</h1>
      <h1>Products</h1>
      {loading ? (
        <Loader />
      ) : error ? (
        <Message variant="danger">{error}</Message>
      ) : (
        <Row>
          {products.map((p) => (
            <Col key={p.id} sm={9} md={6} lg={4} xl={3}>
              <Product product={p} />
            </Col>
          ))}
        </Row>
      )}
      <Footer />
    </div>
  );
};

export default HomePage;
