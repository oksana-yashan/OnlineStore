import { Container, Row } from "react-bootstrap";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import Header from "./components/Header";
import React from 'react';
import Footer from "./components/Footer";
import HomePage from "./pages/HomePage";
import ProductPage from "./pages/ProductPage";
import CartPage from "./pages/CartPage";
import LoginPage from "./pages/LoginPage";
import RegisterPage from "./pages/RegisterPage";
import ProfilePage from "./pages/ProfilePage";
import ShippingPage from "./pages/ShippingPage";
import PaymentPage from "./pages/PaymentPage";
import { createBrowserHistory } from 'history'
import { withRouter } from 'react-router';

import PlaceOrderPage from './pages/PlaceOrderPage';
import OrderPage from './pages/OrderPage';
import UserListPage from './pages/admin/UserListPage';
import UserEditPage from './pages/admin/UserEditPage';
import ProductListPage from "./pages/admin/ProductListPage";
import ProductEditPage from './pages/admin/ProductEditPage';
import OrderListPage from "./pages/admin/OrderListPage";


export const history = createBrowserHistory()

class App extends React.Component {

  render() { 
    return ( 
      <BrowserRouter history={history}>
      <Header />
      <Switch>
        <Route path="/" component={HomePage} exact />
        <Route path="/product/:id" component={ProductPage} />
        <Route path="/cart/:id?" component={CartPage} />
        <Route path="/login" component={LoginPage} />
        <Route path="/register" component={RegisterPage} />
        <Route path="/profile" component={ProfilePage} />
        <Route path="/shipping" component={ShippingPage} />
        <Route path='/payment' component={PaymentPage} />
        <Route path='/placeorder' component={PlaceOrderPage} />
        <Route path='/order/:id' component={OrderPage} />
        <Route path='/admin/userlist' component={UserListPage}/>
        <Route path='/admin/user/:id/edit/' component={UserEditPage}/>
        
        <Route path='/admin/productlist' component={ProductListPage}/>
        <Route path='/admin/product/:id/edit/' component={ProductEditPage}/>
        
        <Route path='/admin/orderlist' component={OrderListPage}/>
        

      </Switch>
    </BrowserRouter>
     );
  }
}
 
export default App;
// export history;


// function App() {
//   return (
//     <BrowserRouter>
//       <Header {...props}/>
//       <Switch>
//         <Route path="/" component={HomePage} exact />
//         <Route path="/product/:id" component={ProductPage} />
//         <Route path="/cart/:id?" component={CartPage} />
//         <Route path="/login" component={LoginPage} />
//         <Route path="/register" component={RegisterPage} />
//         <Route path="/profile" component={ProfilePage} />
//         <Route path="/shipping" component={ShippingPage} />
//         <Route path='/payment' component={PaymentPage} />
//         <Route path='/placeorder' component={PlaceOrderPage} />
//         <Route path='/order/:id' component={OrderPage} />
//         <Route path='/admin/userlist' component={UserListPage}/>
//       </Switch>
//     </BrowserRouter>
//   );
// }

// export default App;
