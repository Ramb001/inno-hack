import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const baseApi = createApi({
  tagTypes: [],

  baseQuery: fetchBaseQuery({
    baseUrl: "http://46.17.248.71:8000/",
  }),
  endpoints: () => ({}),
});
