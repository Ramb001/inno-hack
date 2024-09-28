export type GetOrganizationDtoResponse = {
  id: number;
  ref_lin: string;
  name: string;
  owner_id: number;
}[];
export type GetOrganizationDtoRequest = void;
export type CreateOrganizationDtoResponse = {
  organization_id: number;
  message: string;
};
export type CreateOrganizationDtoRequest = {
  name: string;
  ref_link: string;
  owner_id: number;
};
export type DeleteOrganizationDtoResponse = {
  message: string;
};
export type DeleteOrganizationDtoRequest = {
  organization_id: number;
};
export type GetOrganizationInfoDtoResponse = {
  status: string;
  id: number | string;
}[];
export type GetOrganizationInfoDtoRequest = {
  organization_id: number;
};
export type CreateOrganizationStatuesDtoResponse = {
  message: string;
}[];
export type CreateOrganizationStatuesDtoRequest = {
  organization_id: number;
  status: string;
};
