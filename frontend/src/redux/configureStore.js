//redux Store를 설정/구성한다.(Reducer 합치기)
import { createStore, combineReducers } from 'redux';
import users from 'redux/modules/users';

const reducer = combineReducers({ //combineReducer로 reducer들을 합친다.
    users
})

let store = initialState => createStore(reducer);

export default store();