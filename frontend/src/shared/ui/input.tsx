import * as React from "react";

import { cn } from "@/shared/lib/utils";

export interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label?: string;
  labelTag?: string;
}

const InputWithLabel = React.forwardRef<HTMLInputElement, InputProps>(
  ({ label, labelTag, className, type, ...props }, ref) => {
    return (
      <div className="grid w-full items-center gap-1.5">
        <label className="text-sm" htmlFor={labelTag}>
          {label}
        </label>
        <input
          type={type}
          className={cn(
            "flex h-10 rounded-md w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium file:text-foreground placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50",
            className
          )}
          ref={ref}
          {...props}
        />
      </div>
    );
  }
);
InputWithLabel.displayName = "InputWithLabel";

export { InputWithLabel };
