import {createStore, combineReducers, applyMiddleware} from 'redux'
import thunk from 'redux-thunk';
import {composeWithDevTools} from 'redux-devtools-extension';
import {productListReducer,
    productDetailsReducer, productImagesReducer} from './reducers/productReducers'
import { cartReducer } from './reducers/cartReducers';
import { userLoginReducer, userRegisterReducer, userDetailsReducer, userUpdateProfileReducer } from './reducers/userReducer';

const reducers = combineReducers({
    productList: productListReducer,
    productDetails: productDetailsReducer,
    productImages: productImagesReducer,

    cart: cartReducer,
    userLogin : userLoginReducer,
    userRegister : userRegisterReducer,
    userDetails: userDetailsReducer,
    userUpdateProfile : userUpdateProfileReducer,
})

const cartItemsFromStorage = localStorage.getItem('cartItems') ?
    JSON.parse(localStorage.getItem('cartItems')) : []

const userInfoFromStorage = localStorage.getItem('userInfo') ?
    JSON.parse(localStorage.getItem('userInfo')) : null



const initialState = {
    cart:{cartItems: cartItemsFromStorage},
    userLogin:{userInfo: userInfoFromStorage}
        
}

const middleware = [thunk]

const store = createStore(reducers, initialState, 
    composeWithDevTools(applyMiddleware(...middleware)))

export default store;