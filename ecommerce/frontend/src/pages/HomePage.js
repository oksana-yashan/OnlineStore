import React, { useEffect, useState } from "react";
import { Row, Col, Button, Dropdown } from "react-bootstrap";
import Product from "../components/Product";
import { listProducts } from "../actions/productActions";
import Loader from "../components/Loader";
import Message from "../components/Message";
import { useDispatch, useSelector } from "react-redux";
import Footer from "../components/Footer";
import Paginate from "../components/Paginate";
import ProductCarousel from "../components/ProductCarousel";
import Categories from "../components/Categories";
import { Link } from "react-router-dom";

const HomePage = ({ history }) => {
  //  const [products, setProducts] = useState([]);
  const dispatch = useDispatch();
  const productList = useSelector((state) => state.productList);
  const { error, loading, products,categories, page, pages } = productList;

  let search = history.location.search;
  const [filter, setFilter] = useState("");
  const [sorting, setSorting] = useState("");

  useEffect(() => {
    dispatch(listProducts(search, filter, sorting));
  }, [dispatch, search, filter, sorting]);


  return (
    <div>
      {!search && <ProductCarousel />}

      {/* <h1 >Products</h1> */}
      {loading ? (
        <Loader />
      ) : error ? (
        <Message variant="danger">{error}</Message>
      ) : (
        <div>
          <div class="row" style={{"justifyContent":"left"}}>
          <Dropdown>
                <Dropdown.Toggle variant="success" id="dropdown-basic">
                  Sort by
                </Dropdown.Toggle>

                <Dropdown.Menu>
                  <Dropdown.Item onClick={() => setSorting(`ordering=price`)}>Price <i class="fa fa-arrow-up"></i></Dropdown.Item>
                  <Dropdown.Item onClick={() => setSorting(`ordering=-price`)}>Price <i class="fa fa-arrow-down"></i></Dropdown.Item>
                  <Dropdown.Item onClick={() => setSorting(`ordering=raiting`)}>Raiting <i class="fa fa-arrow-up"></i></Dropdown.Item>
                  <Dropdown.Item onClick={() => setSorting(`ordering=-raiting`)}>Raiting <i class="fa fa-arrow-down" ></i></Dropdown.Item>
                </Dropdown.Menu>
              </Dropdown>
          </div>

          <div class="row">
            <div class="my-sidebar">
              {/* <Categories categories={categories}/> */}
              <menu>
                  <div id={0}>
                   <Link to={"/"} onClick={() => setFilter("")}>{"All Categories"}</Link>
                  </div>
                {categories.map((category) => (
                  <div id={category.id}>
                   <Link to={"/"} onClick={() => setFilter(`categories=${category.id}`)}>{category.name}</Link>
                  </div>
                ))}

              </menu>
            </div>
            
            <div class="col text-center">
              <Row>
              
                {products.map((p) => (
                  <Col key={p.id} sm={9} md={6} lg={4} xl={3}>
                    <Product product={p} />
                  </Col>
                ))}
              </Row>
            </div>
          </div>
          
          <Paginate page={page} pages={pages} search={search} />
        </div>
      )}
      <Footer />
    </div>
  );
};

export default HomePage;
