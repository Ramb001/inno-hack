export const Header = () => {
  return (
    <header className="flex items-center justify-between h-20 w-full px-8  text-black border-b border-gray-200 shadow-lg">
      <div className="flex items-center">
        <span className="ml-4 text-lg uppercase">
          Управление проектами легко!
        </span>
      </div>
      <nav className="flex space-x-4">
        <a href="#" className="hover:text-gray-200 transition">
          Главная
        </a>
        <a href="#" className="hover:text-gray-200 transition">
          Задачи
        </a>
        <a href="#" className="hover:text-gray-200 transition">
          О проекте
        </a>
      </nav>
      <button className="bg-white px-4 py-2 rounded-lg shadow hover:bg-gray-200 transition">
        Выйти
      </button>
    </header>
  );
};
