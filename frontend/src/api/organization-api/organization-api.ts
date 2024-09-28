import { baseApi } from "@/shared/api/base-api";
import { GetOrganizationDtoRequest, GetOrganizationDtoResponse } from "./types";

export const organizationApi = baseApi.injectEndpoints({
  endpoints: (builder) => ({
    getOrganization: builder.query<
      GetOrganizationDtoRequest,
      GetOrganizationDtoResponse
    >({
      query: () => ({ url: `organizations/organizations` }),
    }),
  }),
});
export const { useGetOrganizationQuery } = organizationApi;
