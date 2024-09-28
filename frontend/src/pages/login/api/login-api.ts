import { baseApi } from "@/shared/api/base-api";

const loginApi = baseApi.injectEndpoints({
  endpoints: (builder) => ({
    login: builder.mutation({
      query: (user) => ({
        url: "users/login",
        method: "POST",
        body: user,
      }),
    }),
    register: builder.mutation({
      query: (newUser) => ({
        url: "users/register",
        method: "POST",
        body: newUser,
      }),
    }),
  }),
});

export const { useLoginMutation, useRegisterMutation } = loginApi;
