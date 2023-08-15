#!/usr/bin/python3
"""Module for entry point of the command interpreter."""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone project."""

    prompt = "(hbnb)"

    def do_quit(self, args):
        """Exit the program."""
        return True

    def do_EOF(self, args):
        """Exit the prorm."""
        print()
        return True

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return
        new_instance = storage.classes()[class_name]()
        storage.save()
        print(new_instance.id)

    def do_show(self, args):
        """Print the string representation of an instance."""
        if not args:
            print("** class name missing **")
            return

        args_list = args.split()
        class_name = args_list[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(args_list) < 2:
            print("** instance id missing **")
            return

        instances = storage.all()
        obj_id = args_list[1]
        obj_key = "{}.{}".format(class_name, obj_id)
        if obj_key in instances:
            print(instances[obj_key])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """Delete an instance based on the class name and id."""
        args = args.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in [cls.__name__
                             for cls in BaseModel.__subclasses__()]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_dict = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in obj_dict:
                del obj_dict[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances"""
        args = line.split()
        if args and args[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            instances = storage.all()
            print([str(instance) for instance in instances.values()])

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instances = storage.all()
        obj_id = args[1]
        obj_key = "{}.{}".format(class_name, obj_id)
        if obj_key not in instances:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_name = args[2]
        attribute_value = args[3]
        instance = instances[obj_key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
