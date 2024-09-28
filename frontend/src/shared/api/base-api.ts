import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const baseApi = createApi({
  tagTypes: [],

  baseQuery: fetchBaseQuery({
    baseUrl: "https://jsonplaceholder.typicode.com/'",
  }),
  endpoints: () => ({}),
});
