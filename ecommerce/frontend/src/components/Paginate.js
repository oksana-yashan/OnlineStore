import React from 'react'
import { Pagination } from 'react-bootstrap'
import { LinkContainer } from 'react-router-bootstrap'

function Paginate({ pages, page, search = '', is_admin = false }) {
    if (search.includes("?search=")) {
        search = search.split('?search=')[1].split('&')[0]
    }
    

    return (pages > 1 && (
        <Pagination>
            {[...Array(pages).keys()].map((x) => {
                // let url = search ? `/?search=${search}&page=${x + 1}` : `/?page=${x + 1}`
                let url = `/?search=${search}&page=${x + 1}`

                return <LinkContainer
                    key={x + 1}
                    to={!is_admin ?
                        url
                        : `/admin/productlist/${url}`
                    }
                >
                    <Pagination.Item active={x + 1 === page}>{x + 1}</Pagination.Item>
                </LinkContainer>
            })}
        </Pagination>
    )
    )
}

export default Paginate
