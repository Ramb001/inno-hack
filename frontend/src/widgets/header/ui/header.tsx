import { Profile } from "@/widgets/profile";

export const Header = () => {
  return (
    <header className="flex flex-row-reverse items-center justify-between h-20 w-full px-8  text-black border-b border-gray-200 shadow-lg">
      <Profile />
    </header>
  );
};
