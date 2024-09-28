import { baseApi } from "@/shared/api/base-api";
import {
  CreateOrganizationDtoRequest,
  CreateOrganizationDtoResponse,
  CreateOrganizationStatuesDtoRequest,
  CreateOrganizationStatuesDtoResponse,
  DeleteOrganizationDtoRequest,
  DeleteOrganizationDtoResponse,
  GetOrganizationDtoRequest,
  GetOrganizationDtoResponse,
  GetOrganizationInfoDtoRequest,
  GetOrganizationInfoDtoResponse,
} from "./types";

export const organizationApi = baseApi.injectEndpoints({
  endpoints: (builder) => ({
    getOrganization: builder.query<
      GetOrganizationDtoResponse,
      GetOrganizationDtoRequest
    >({
      query: () => ({ url: `organizations/organizations`, method: "GET" }),

      providesTags: ["ORGANIZATION"],
    }),
    createOrganization: builder.mutation<
      CreateOrganizationDtoResponse,
      CreateOrganizationDtoRequest
    >({
      query: (props) => ({
        url: `organizations/create`,
        body: props,
        method: "POST",
      }),
      invalidatesTags: ["ORGANIZATION"],
    }),
    deleteOrganization: builder.mutation<
      DeleteOrganizationDtoResponse,
      DeleteOrganizationDtoRequest
    >({
      query: ({ organization_id }) => ({
        url: `organizations/${organization_id}/delete`,
        method: "DELETE",
      }),
      invalidatesTags: ["ORGANIZATION"],
    }),
    getOrganizationInfoColumns: builder.query<
      GetOrganizationInfoDtoResponse,
      GetOrganizationInfoDtoRequest
    >({
      query: ({ organization_id }) => ({
        url: `/organizations/${organization_id}/info/statuses`,
        method: "GET",
      }),
    }),
    createOrganizationColumns: builder.mutation<
      CreateOrganizationStatuesDtoResponse,
      CreateOrganizationStatuesDtoRequest
    >({
      query: ({ organization_id, status }) => ({
        url: `organizations/${organization_id}/info/statuses/create`,
        method: "POST",
        body: status,
      }),
      invalidatesTags: ["ORGANIZATION"],
    }),
  }),
});
export const {
  useGetOrganizationQuery,
  useCreateOrganizationMutation,
  useDeleteOrganizationMutation,
  useGetOrganizationInfoColumnsQuery,
  useCreateOrganizationColumnsMutation,
} = organizationApi;
