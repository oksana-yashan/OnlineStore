import axios from "axios";
import {
  CART_ADD_ITEM,
  CART_REMOVE_ITEM,
  CART_SAVE_SHIPPING_ADDRESS,
  CART_SAVE_PAYMENT_METHOD,
  CART_FETCH,
} from "../constants/cartConstants";
import { getState } from "react-redux";
import { history } from "../App";


const getConfig = (getState) => {
  const {
    userLogin: { userInfo },
  } = getState();

  const config = {
    headers: {
      "Content-type": "application/json",
      Authorization: `Bearer ${userInfo.token}`,
    },
  };
  return config;
};

export const fetchCart = () => async (dispatch, getState) => {
  
  const { data } = await axios.get("/cart/current/", getConfig(getState));
  const items = data.cart_items;
  console.log(items);

  dispatch({ type: CART_FETCH, payload: items });
  localStorage.setItem("cartItems", JSON.stringify(getState().cart.cartItems));

};

export const addToCart = (id, qty) => async (dispatch, getState) => {

  const params = { "quantity": qty, "product": parseInt(id) };
  console.log(JSON.parse(JSON.stringify(params)));

  const {
    userLogin: { userInfo },
  } = getState();

  const config = {
    headers: {
      "Content-type": "application/json",
      Authorization: `Bearer ${userInfo.token}`,
    },
  };


  const { data: cart_item_info } = await axios.post(
    "/cart/current/",
    {product: id, quantity: qty },
    getConfig(getState)
  );

  let { data: item } = await axios.get(
    `/cart/current/${cart_item_info.id}/`,
    getConfig(getState)
  );

  dispatch({
    type: CART_ADD_ITEM,
    payload: { ...item },
  });
  localStorage.setItem("cartItems", JSON.stringify(getState().cart.cartItems));
};

export const removeFromCart = (item_id) => async (dispatch, getState) => {

  await axios.delete(`/cart/current/${item_id}`, getConfig(getState));

  dispatch({
    type: CART_REMOVE_ITEM,
    payload: item_id,
  });

  localStorage.setItem("cartItems", JSON.stringify(getState().cart.cartItems));
};

export const saveShippingAddress = (data) => (dispatch) => {
  dispatch({
    type: CART_SAVE_SHIPPING_ADDRESS,
    payload: data,
  });

  localStorage.setItem("shippingAddress", JSON.stringify(data));
};

export const savePaymentMethod = (data) => (dispatch) => {
  dispatch({
    type: CART_SAVE_PAYMENT_METHOD,
    payload: data,
  });

  localStorage.setItem("paymentMethod", JSON.stringify(data));
};
