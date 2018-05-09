//redux Store를 설정/구성한다.(Reducer 합치기)
import { createStore, combineReducers, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import users from 'redux/modules/users';

const middlewares = [thunk];

const reducer = combineReducers({ //combineReducer로 reducer들을 합친다.
    users
})

let store = initialState => createStore(reducer, applyMiddleware(...middlewares)); // For make list of function, use "..." it means, unpack the array

export default store(); 