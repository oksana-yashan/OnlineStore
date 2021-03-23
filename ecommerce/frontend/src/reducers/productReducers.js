import {
    PRODUCT_LIST_REQUEST,
    PRODUCT_LIST_SUCCESS,
    PRODUCT_LIST_FAIL,

    PRODUCT_DETAILS_REQUEST,
    PRODUCT_DETAILS_SUCCESS,
    PRODUCT_DETAILS_FAIL,

    PRODUCT_IMAGES_REQUEST,
    PRODUCT_IMAGES_SUCCESS,
    PRODUCT_IMAGES_FAIL
} from '../constants/productConstants'


export const productListReducer = (state = { products: [] }, action) => {
    switch (action.type) {
        case PRODUCT_LIST_REQUEST:
            return { loading: true, products: [] }

        case PRODUCT_LIST_SUCCESS:
            return {
                loading: false,
                products: action.payload
            }

        case PRODUCT_LIST_FAIL:
            return { loading: false, error: action.payload }

        default:
            return state
    }
}



export const productDetailsReducer = (state = { product: [], images:""}, action) => {
    switch (action.type) {
        case PRODUCT_DETAILS_REQUEST:
            return { loading: true, ...state }

        case PRODUCT_DETAILS_SUCCESS:
            //console.log(action.payload)
            return { loading: false, product: action.payload[0], images:action.payload[1] }

        case PRODUCT_DETAILS_FAIL:
            return { loading: false, error: action.payload }

        default:
            return state
    }
}



export const productImagesReducer = (state = { images: ""}, action) => {
    switch (action.type) {
        case PRODUCT_IMAGES_REQUEST:
            return { loading: true, ...state }

        case PRODUCT_IMAGES_SUCCESS:
            //console.log(action.payload)
            return { loading: false, images:action.payload }

        case PRODUCT_IMAGES_FAIL:
            return { loading: false, error: action.payload }

        default:
            return state
    }
}


