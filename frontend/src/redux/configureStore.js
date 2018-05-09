//redux Store를 설정/구성한다.(Reducer 합치기)
import { createStore, combineReducers, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import users from 'redux/modules/users';

const env = process.env.NODE_ENV; //process는 nodejs의 전체정보를 가지고 있는 Variable이다.

const middlewares = [thunk];

if(env === "development"){ //dev 환경일때만 logger를 부른다.(prod일 경우 부르지 않는다.)
    const { logger } = require("redux-logger")
    middlewares.push(logger); //middlewares array를 만든이유는 dev에서 추가할 수도 있기 때문이다.
} //dev가 아닐때 array는 thunk이다. 하지만 dev일때는 logger도 있다.

const reducer = combineReducers({ //combineReducer로 reducer들을 합친다.
    users
})

let store = initialState => createStore(reducer, applyMiddleware(...middlewares)); // For make list of function, use "..." it means, unpack the array

export default store(); 