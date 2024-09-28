import { useDeleteOrganizationMutation } from "@/api/organization-api/organization-api";
import { X } from "lucide-react";

type OrganizationDeleteProps = {
  id: number;
};
export const OrganizationDelete = (props: OrganizationDeleteProps) => {
  const { id } = props;
  const [deleteOrganization] = useDeleteOrganizationMutation();
  const onClick = (e: React.MouseEvent<HTMLButtonElement, MouseEvent>) => {
    e.stopPropagation();
    deleteOrganization({
      organization_id: id,
    });
  };
  return (
    <button onClick={(e) => onClick(e)}>
      <X className="" />
    </button>
  );
};
