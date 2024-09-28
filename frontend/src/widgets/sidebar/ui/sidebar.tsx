import { useGetOrganizationQuery } from "@/api/organization-api/organization-api";
import { OrganizationCreate } from "@/components/organization/organization-create";
import { OrganizationItem } from "@/components/organization/organization-item";

import { Button } from "@/shared/ui/button";
import { HomeIcon, PlusSquare, Settings, UserRound } from "lucide-react";

export const Sidebar = () => {
  const { data: organizations } = useGetOrganizationQuery();

  return (
    <aside className="h-screen w-[300px] border-r border-gray-200 p-6 flex flex-col gap-6 shadow-lg">
      <p className="text-2xl font-bold text-gray-800 border-b pb-2">
        TASK MANAGER
      </p>
      <div className="flex flex-col gap-4 p-4 rounded-xl bg-gray-50 shadow-inner">
        <div className="flex items-center gap-4 hover:bg-gray-200 p-2 rounded-xl transition duration-200 cursor-pointer">
          <HomeIcon className="text-gray-600" />
          <p className="text-gray-700">Главная</p>
        </div>

        <div className="flex items-center gap-4 hover:bg-gray-200 p-2 rounded-xl transition duration-200 cursor-pointer">
          <UserRound className="text-gray-600" />
          <p className="text-gray-700">Участники</p>
        </div>

        <div className="flex items-center gap-4 hover:bg-gray-200 p-2 rounded-xl transition duration-200 cursor-pointer">
          <Settings className="text-gray-600" />
          <p className="text-gray-700">Настройки</p>
        </div>
      </div>

      <hr className="border-gray-300" />

      <div className="flex items-center justify-between">
        <p className="text-gray-800 font-semibold">МОИ ОРГАНИЗАЦИИ</p>
        <OrganizationCreate />
      </div>

      <div className="flex flex-col border rounded-xl gap-3 p-4 bg-gray-50 shadow-inner">
        {organizations?.map((organization) => (
          <OrganizationItem key={organization.id} name={organization.name} />
        ))}
      </div>
    </aside>
  );
};
