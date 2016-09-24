import { combineReducers } from 'redux'

import { RECEIVE_CONFIG } from '../actions'


function config(state = {}, action) {
  switch (action.type) {
    case RECEIVE_CONFIG:
      return action.config
    default:
      return state
  }
}

const rootReducer = combineReducers({
  config
})

export default rootReducer
