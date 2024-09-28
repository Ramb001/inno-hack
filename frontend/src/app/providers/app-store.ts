import { baseApi } from "@/shared/api/base-api";
import { combineReducers, configureStore } from "@reduxjs/toolkit";
import { TypedUseSelectorHook, useDispatch, useSelector } from "react-redux";
const rootReducers = combineReducers({
  [baseApi.reducerPath]: baseApi.reducer,
});

export const createStore = () => {
  const store = configureStore({
    reducer: rootReducers,
    devTools: true,
    middleware: (gDM) => gDM().concat(baseApi.middleware),
  });
  return store;
};

export const appStore = createStore();

export type RootState = ReturnType<typeof appStore.getState>;

export type AppDispatch = typeof appStore.dispatch;

export const useAppDispatch = useDispatch<AppDispatch>;
export const useAppSelector: TypedUseSelectorHook<RootState> = useSelector;
