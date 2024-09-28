import { TaskDragData } from "@/components/task-card";
import { ColumnDragData } from "@/components/task-column";
import { Active, DataRef, Over } from "@dnd-kit/core";

type DraggableData = ColumnDragData | TaskDragData;

export function hasDraggableData<T extends Active | Over>(
  entry: T | null | undefined
): entry is T & {
  data: DataRef<DraggableData>;
} {
  if (!entry) {
    return false;
  }

  const data = entry.data.current;

  if (data?.type === "Column" || data?.type === "Task") {
    return true;
  }

  return false;
}
