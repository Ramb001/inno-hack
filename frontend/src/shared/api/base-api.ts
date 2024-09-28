import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";
const ORGANIZATION_TAG = "ORGANIZATION";
export const baseApi = createApi({
  tagTypes: [ORGANIZATION_TAG],

  baseQuery: fetchBaseQuery({
    baseUrl: "https://api.stask-bot.online/",
  }),
  endpoints: () => ({}),
});
