import { Task } from "@/components/task-card";
import { KanbanBoard, TaskTable } from "@/components/task-table";
const mockTasks: Task[] = [
  {
    status: "Completed",
    title: "Разработка главной страницы",
    content: "Завершить адаптивную верстку главной страницы",
    members: ["Иван", "Алексей"],
    id: 1,
    columnId: 1,
  },
  {
    status: "High",
    title: "Тестирование API",
    content: "Написать тесты для всех эндпоинтов API",
    members: ["Мария", "Олег"],
    id: 2,
    columnId: 2,
  },
  {
    status: "Low",
    title: "Подготовка документации",
    content: "Создать руководство пользователя для нового приложения",
    members: ["Светлана", "Иван"],
    id: 3,
    columnId: 1,
  },
  {
    status: "Completed",
    title: "Оптимизация базы данных",
    content: "Улучшить производительность запросов к базе данных",
    members: ["Александр", "Юлия"],
    id: 4,
    columnId: 1,
  },
  {
    status: "High",
    title: "Рефакторинг кода",
    content: "Провести рефакторинг старого кода проекта",
    members: ["Ольга", "Максим"],
    id: 5,
    columnId: 1,
  },
  {
    status: "Low",
    title: "Обновление зависимостей",
    content: "Обновить устаревшие библиотеки и пакеты",
    members: ["Алексей", "Дмитрий"],
    id: 6,
    columnId: 1,
  },
  {
    status: "Completed",
    title: "Создание лендинга",
    content: "Разработать лендинг для маркетинговой кампании",
    members: ["Мария", "Анастасия"],
    id: 7,
    columnId: 1,
  },
  {
    status: "High",
    title: "Разработка новой функции",
    content: "Добавить возможность импорта/экспорта данных",
    members: ["Иван", "Олег"],
    id: 8,
    columnId: 1,
  },
  {
    status: "Low",
    title: "Очистка кода",
    content: "Удалить неиспользуемые переменные и функции",
    members: ["Максим", "Ольга"],
    id: 9,
    columnId: 1,
  },
  {
    status: "Completed",
    title: "Настройка CI/CD",
    content: "Настроить автоматическую сборку и деплой проекта",
    members: ["Александр", "Юлия"],
    id: 10,
    columnId: 1,
  },
];

export const MainPage = () => {
  return (
    <section>
      <KanbanBoard />
    </section>
  );
};
