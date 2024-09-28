type OrganizationItemProps = {
  name: string;
};
export const OrganizationItem = (props: OrganizationItemProps) => {
  const { name } = props;
  return (
    <div className="hover:bg-gray-100 p-3 hover:cursor-pointer flex items-center hover:font-medium hover:rounded-xl gap-4">
      <span className="w-2 h-2 rounded-full bg-green-500" />
      <p>{name}</p>
    </div>
  );
};
