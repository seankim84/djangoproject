// imports

// actions

// action creators

// initial state
const initialState = {
    isLoggedIn: localStorage.getItem('jwt')|| false //localStorage안으로 들어가서 jwt를 찾는다.

}

// reducer
function reducer(state= initialState, action){
    switch(action.type){
        default:
            return state;
    }
}

// reducer function

// exports
export default reducer;

// reducer export