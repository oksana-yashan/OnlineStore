import axios from 'axios'
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


export const listProducts = () => async (dispatch) => {
    try {
        dispatch({ type: PRODUCT_LIST_REQUEST })

        const { data } = await axios.get(`/products`)
        //console.log(data.results)

        dispatch({
            type: PRODUCT_LIST_SUCCESS,
            payload: data.results
            
        })

    } catch (error) {
        dispatch({
            type: PRODUCT_LIST_FAIL,
            payload: error.response && error.response.data.detail
                ? error.response.data.detail
                : error.message,
        })
    }
}



export const listProductDetails = (id) => async (dispatch) => {
    try {
        dispatch({ type: PRODUCT_DETAILS_REQUEST })

        const { data:product } = await axios.get(`/products/${id}`)
        const { data:image } = await axios.get(`/products/${id}/media`)
        //console.log(images.results[0].image)
        let images = []
        if (image.results[0])
            images.push(image.results[0].image)
        else
            images.push(product.image)

        dispatch({
            type: PRODUCT_DETAILS_SUCCESS,
            payload: [product, images]
        })

    } catch (error) {
        dispatch({
            type: PRODUCT_DETAILS_FAIL,
            payload: error.response && error.response.data.detail
                ? error.response.data.detail
                : error.message,
        })
    }
}


export const productImages = (id) => async (dispatch) => {
    try {
        dispatch({ type: PRODUCT_IMAGES_REQUEST })

       const { data:images } = await axios.get(`products/${id}/media`)
        //console.log(images.results[0].image)

        dispatch({
            type: PRODUCT_IMAGES_SUCCESS,
            payload: images.results[0].image
        })

    } catch (error) {
        dispatch({
            type: PRODUCT_IMAGES_FAIL,
            payload: error.response && error.response.data.detail
                ? error.response.data.detail
                : error.message,
        })
    }
}
