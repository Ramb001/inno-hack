import { Link } from "react-router-dom";
import { OrganizationDelete } from "../../organization-delete";

type OrganizationItemProps = {
  name: string;
  organizationId: number;
};
export const OrganizationItem = (props: OrganizationItemProps) => {
  const { name, organizationId } = props;

  return (
    <div className="hover:bg-gray-100 p-3 hover:cursor-pointer flex items-center justify-between hover:font-medium hover:rounded-xl gap-4">
      <Link
        className="flex items-center gap-4"
        to={`/board/:${organizationId}`}
      >
        <span className="w-2 h-2 rounded-full bg-green-500" />
        <p>{name}</p>
      </Link>
      <OrganizationDelete id={organizationId} />
    </div>
  );
};
